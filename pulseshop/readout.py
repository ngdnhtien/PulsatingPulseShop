"""
Readout: turning single-shot IQ points into |0>, |1>, |2> populations, and
correcting those populations for readout (SPAM) errors.

Three generations of discriminators coexist in the project:

* `LDADiscriminator`  -- scikit-learn linear discriminant analysis trained on
  the three calibration circuits (2022-2024, "lineage B" / Qiskit textbook).
* `CentroidDiscriminator` -- nearest cluster centre, with an optional radius
  that flags outliers (2025, `discrim.ipynb`, `T1_script.ipynb`).
* `RadiusDiscriminator` -- the 2025 paper discriminator: a point is |0> or |2>
  if it falls inside a circle of radius `radius_fit` around the |0> / |2>
  cluster means fitted on a Rabi oscillation; everything else is |1>, except
  that points left of the |0> circle (Re<0) count as |0> and points below the
  |2> circle (Im<0) count as |2> (`rabi_discrim.pkl`, `phase_advance_plot`).

Readout mitigation is the constrained least squares  min ||C^T x - p||  with
x >= 0, sum x = 1, solved either with SLSQP (`utility.data_mitigator`) or as a
cvxopt quadratic programme (lineage B `mitigated_population`).
"""

import numpy as np
from scipy.optimize import minimize

try:
    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
    from sklearn.model_selection import train_test_split
except ImportError:  # pragma: no cover
    LinearDiscriminantAnalysis = None

from .fitting import distance


# ------------------------------------------------------------ utilities ----
def reshape_complex_vec(vec):
    """Complex IQ vector -> (N, 2) real array [Re, Im] (needed by scikit-learn)."""
    vec = np.asarray(vec).ravel()
    return np.column_stack([np.real(vec), np.imag(vec)])


def iq_012_plot(discrim_data, ax=None, s=0.5, alpha=0.5, title="0-1-2 discrimination", limits=None):
    """Scatter the |0>, |1>, |2> calibration shots in the IQ plane with their means."""
    import matplotlib.pyplot as plt
    ax = ax or plt.gca()
    colors = ["tab:blue", "tab:red", "tab:green"]
    for k, (pts, c) in enumerate(zip(discrim_data, colors)):
        pts = np.asarray(pts).ravel()
        ax.scatter(np.real(pts), np.imag(pts), s=s, c=c, alpha=alpha, label=rf"$|{k}\rangle$")
        m = np.mean(pts)
        ax.scatter(np.real(m), np.imag(m), s=120, c="black", zorder=5)
    if limits is not None:
        ax.set_xlim(limits[0], limits[1]); ax.set_ylim(limits[2], limits[3])
    ax.legend(markerscale=10)
    ax.set_xlabel("I [a.u.]"); ax.set_ylabel("Q [a.u.]"); ax.set_title(title)
    return ax


# ------------------------------------------------------- discriminators ----
class LDADiscriminator:
    """Linear discriminant analysis on (Re, Im), trained on |0>,|1>,|2> shots."""

    def __init__(self, test_size=0.3, random_state=None):
        if LinearDiscriminantAnalysis is None:
            raise ImportError("scikit-learn is required for LDADiscriminator")
        self.test_size = test_size
        self.random_state = random_state
        self.lda = None
        self.score = None

    def fit(self, discrim_data):
        """discrim_data: list of three complex arrays (shots prepared in |0>,|1>,|2>)."""
        xs, ys = [], []
        for label, shots in enumerate(discrim_data):
            r = reshape_complex_vec(shots)
            xs.append(r); ys.append(np.full(len(r), float(label)))
        X = np.concatenate(xs); y = np.concatenate(ys)
        Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=self.test_size, random_state=self.random_state)
        self.lda = LinearDiscriminantAnalysis().fit(Xtr, ytr)
        self.score = self.lda.score(Xte, yte)
        return self

    def predict(self, shots):
        return self.lda.predict(reshape_complex_vec(shots)).astype(int)

    def separatrix(self, ax=None, xlim=None, ylim=None, n=200):
        """Draw the LDA decision regions (textbook `separatrixPlot`)."""
        import matplotlib.pyplot as plt
        ax = ax or plt.gca()
        xlim = xlim or ax.get_xlim(); ylim = ylim or ax.get_ylim()
        xx, yy = np.meshgrid(np.linspace(*xlim, n), np.linspace(*ylim, n))
        zz = self.lda.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
        ax.contour(xx, yy, zz, levels=[0.5, 1.5], colors="black", linewidths=1)
        return ax


class CentroidDiscriminator:
    """
    Nearest cluster centre in the IQ plane (2025).  `centres` is a (3, 2)
    array [[I0, Q0], [I1, Q1], [I2, Q2]]; shots further than `radius` from
    every centre are flagged as outliers but still assigned to the nearest.
    """

    def __init__(self, centres, radius=None):
        self.centres = np.asarray(centres, dtype=float)
        self.radius = radius

    @classmethod
    def from_shots(cls, discrim_data, radius=None):
        centres = [[np.real(np.mean(s)), np.imag(np.mean(s))] for s in discrim_data]
        return cls(centres, radius)

    def predict(self, shots, return_distance=False):
        pts = reshape_complex_vec(shots)
        d = np.linalg.norm(pts[:, None, :] - self.centres[None, :, :], axis=2)
        labels = np.argmin(d, axis=1)
        if return_distance:
            return labels, d[np.arange(len(labels)), labels]
        return labels


class RadiusDiscriminator:
    """
    Paper (2025) discriminator built from a Rabi oscillation on 1-2:
    `cluster_0_mean`, `cluster_2_mean` (complex) and `radius_fit` =
    distance(c0, c2)/2.  See module docstring for the assignment rule.
    """

    def __init__(self, cluster_0_mean, cluster_2_mean, radius_fit):
        self.c0 = complex(cluster_0_mean)
        self.c2 = complex(cluster_2_mean)
        self.radius = float(radius_fit)

    @classmethod
    def from_dict(cls, d):
        return cls(d["cluster_0_mean"], d["cluster_2_mean"], d["radius_fit"])

    def in_zero(self, point):
        return distance(self.c0, point) < self.radius

    def in_two(self, point):
        return distance(self.c2, point) < self.radius

    def predict(self, shots):
        shots = np.asarray(shots).ravel()
        d0 = np.abs(shots - self.c0); d2 = np.abs(shots - self.c2)
        labels = np.ones(len(shots), dtype=int)
        normal0 = d0 < self.radius
        normal2 = (~normal0) & (d2 < self.radius)
        rest = ~(normal0 | normal2)
        abnormal0 = rest & (np.real(shots) < 0)
        abnormal2 = rest & (~abnormal0) & (np.imag(shots) < 0)
        labels[normal0 | abnormal0] = 0
        labels[normal2 | abnormal2] = 2
        return labels


# ------------------------------------------------- counting populations ----
def count(data, discriminator, num_states=3):
    """Populations (n_circuits, num_states) from a list of single-shot arrays."""
    pops = []
    for shots in data:
        labels = discriminator.predict(np.asarray(shots).ravel())
        pops.append(np.bincount(labels, minlength=num_states)[:num_states] / len(labels))
    return np.array(pops)


def confusion_matrix(discrim_data, discriminator):
    """Row i = populations measured when state |i> was prepared."""
    return count(discrim_data, discriminator)


# ----------------------------------------------------------- mitigation ----
def data_mitigator(raw_data, confusion_mat):
    """
    SLSQP constrained least squares (utility.data_mitigator): find x >= 0 with
    sum x = sum p minimising ||p - C^T x||^2.  Returns the mitigated vector.
    """
    raw_data = np.asarray(raw_data, dtype=float)
    cal_mat = np.transpose(np.asarray(confusion_mat, dtype=float))
    nshots = np.sum(raw_data)

    def fun(x):
        return np.sum((raw_data - cal_mat @ x) ** 2)

    x0 = np.random.rand(len(raw_data)); x0 = x0 / np.sum(x0) * nshots
    cons = {"type": "eq", "fun": lambda x: nshots - np.sum(x)}
    bnds = tuple((0, nshots) for _ in x0)
    res = minimize(fun, x0, method="SLSQP", constraints=cons, bounds=bnds, tol=1e-6)
    return res.x


def mitigated_population(p, C):
    """
    cvxopt quadratic programme (2022-24 textbook-style notebooks): minimise
    ||C^T x - p||^2 subject to x >= 0, sum x = 1, where row i of C is the
    population vector measured when |i> is prepared.  Falls back to
    `data_mitigator` if cvxopt is absent.

    Note: the original helper solved ||C x - p|| (C instead of C^T).  For the
    nearly symmetric confusion matrices of this project the difference is at
    the 1e-2 level; the transpose used here is the physically correct one and
    matches `utility.data_mitigator`.
    """
    try:
        from cvxopt import matrix, solvers
    except ImportError:
        return data_mitigator(p, C)
    C = np.asarray(C, dtype=float); p = np.asarray(p, dtype=float)
    n = len(p)
    M = C.T
    P = matrix(M.T @ M)
    q = matrix(-(M.T @ p))
    G = matrix(-np.eye(n))
    h = matrix(np.zeros(n))
    A = matrix(np.ones((1, n)))
    b = matrix(1.0)
    solvers.options["show_progress"] = False
    sol = solvers.qp(P, q, G, h, A, b)
    return np.array([e for e in sol["x"]])


def mitigate(populations, confusion_mat, method="qp"):
    """Apply readout mitigation row by row to a (n, 3) population array."""
    f = mitigated_population if method == "qp" else data_mitigator
    return np.array([f(p, confusion_mat) for p in np.asarray(populations)])


# ------------------------------------------------- the historical class ----
class DataAnalysis:
    """
    Offline re-implementation of `utility.DataAnalysis` (2023-2025).  The
    original wrapped a live IBM job; this one takes the already-retrieved
    IQ data (list of complex arrays, calibration circuits first) so that the
    saved experiments can be re-analysed without IBM access.

    Attributes mirror the original: IQ_data, IQ_discrim, lda_012, score_012,
    raw_counted, confusion_mat, mitiq_data.
    """

    def __init__(self, iq_data, shots=None, num_states=3):
        self.IQ_data = [np.asarray(x).ravel() for x in iq_data]
        self.shots = shots or len(self.IQ_data[0])
        self.num_states = num_states
        self.IQ_discrim = None
        self.lda_012 = None
        self.score_012 = 0
        self.raw_counted = None
        self.mitiq_data = None
        self.confusion_mat = None

    def build_discrim(self):
        self.IQ_discrim = self.IQ_data[: self.num_states]
        disc = LDADiscriminator(test_size=0.5).fit(self.IQ_discrim)
        self.lda_012 = disc
        self.score_012 = disc.score
        return disc

    def count_pop(self):
        self.raw_counted = count(self.IQ_data, self.lda_012, self.num_states)
        self.confusion_mat = self.raw_counted[: self.num_states]
        return self.raw_counted

    def error_mitiq(self):
        self.mitiq_data = mitigate(self.raw_counted, self.confusion_mat, method="slsqp")[self.num_states:]
        return self.mitiq_data

    def run(self):
        self.build_discrim(); self.count_pop(); self.error_mitiq()
        return self.mitiq_data

    def iq_012_plot(self, *limits):
        return iq_012_plot(self.IQ_discrim, limits=limits or None)

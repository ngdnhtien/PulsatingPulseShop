"""
Loading the saved experiments under data/.

Every hardware run kept in the repository lives in its own folder
`data/<era>/<experiment>/<job_id>/` with

    iq_data.npy   complex array (n_circuits, n_shots) of kerneled IQ points
                  (meas_level=1, single shots) -- or (n_circuits,) of averaged
                  values for 'average' runs
    params.json   what was swept and with which pulses (backend, qubit, date,
                  duration, amplitude, beta, repetitions, phases, ...)

Smaller derived results (populations, fitted centres, confusion matrices) are
plain .npy / .json / .csv files next to them.  `README.md` in data/ lists
everything.
"""

import json
import pathlib
import numpy as np

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data"
FIG_DIR = REPO_ROOT / "figures"


def data_path(*parts):
    return DATA_DIR.joinpath(*parts)


def fig_path(*parts):
    p = FIG_DIR.joinpath(*parts)
    p.parent.mkdir(parents=True, exist_ok=True)
    return p


def load_params(folder):
    with open(pathlib.Path(folder) / "params.json") as f:
        return json.load(f)


def load_job(folder):
    """Return (iq_data, params) of one saved job folder."""
    folder = pathlib.Path(folder)
    if not folder.is_absolute():
        folder = DATA_DIR / folder
    iq = np.load(folder / "iq_data.npy", allow_pickle=False)
    return iq, load_params(folder)


def list_jobs(experiment_dir):
    """Sorted list of job folders (those containing params.json) under a directory."""
    d = pathlib.Path(experiment_dir)
    if not d.is_absolute():
        d = DATA_DIR / d
    return sorted(p for p in d.iterdir() if (p / "params.json").exists())


def load_npy(*parts):
    return np.load(data_path(*parts), allow_pickle=False)


def load_json(*parts):
    with open(data_path(*parts)) as f:
        return json.load(f)


def load_csv(*parts, **kw):
    return np.loadtxt(data_path(*parts), delimiter=",", **kw)


def load_complex_csv(*parts):
    """The 2022 csv files of IQ shots written as python complex literals '(a+bj)'."""
    rows = []
    with open(data_path(*parts)) as f:
        for line in f:
            vals = [v.strip() for v in line.strip().split(",") if v.strip()]
            rows.append(np.array([complex(v) for v in vals]))
    return rows


def save_fig(fig, name, subdir="generated", formats=("png",), dpi=200):
    """Save a matplotlib figure under figures/<subdir>/name.<fmt>."""
    for fmt in formats:
        fig.savefig(fig_path(subdir, f"{name}.{fmt}"), dpi=dpi, bbox_inches="tight")

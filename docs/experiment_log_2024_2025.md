# Experiment log of the paper runs (from `paper/experiment_ids.ipynb`)

*Verbatim notes of the author, one entry per IBM job id; the raw data of most of these jobs are in `data/pending_2025/`, images re-linked to this repository.*

# Rabi oscillation

### 1. Experiment ID: `cxpsz544a290008xhaa0`

Normal Rabi oscillation experiment. Used two $\pi/2$ pulses. Shots was increased to 10k. Focused in range from $-0.1$ to $0.4$ for maximum resolvability of the Rabi amplitude.

The obtained amplitude: `0.2383838383838384`. It fits quite well. Here's the result.

![](../figures/paper_2025/rabi12_q109_cxpsz544a290008xhaa0.png)

### 2. Experiment ID: `cxsfpfswk6yg008ht4s0`

Used just one $\pi$ pulse. Number of shots was 10k. Focused in range from $-0.1$ to $0.6$. The obtained amplitude: `0.4797979797979798`. 

![](../figures/paper_2025/rabi12_q109_cxsfpfswk6yg008ht4s0.png)

### 3. Experiment ID: `cyb4se57v8tg008fxxeg`

*For corrected randomized benchmarking experiments. Used **TWO** $\pi/2$ pulse. Shots was 10k. Migrated to new notebook and new Sampler (in place of backend.run()). 

DID use reset. The obtained amplitude: `0.23678929765886286`. Fits very well.

![](../figures/paper_2025/rabi12_q109_cyb4se57v8tg008fxxeg.png)

# Discriminator

For circuit 0: `cy22fmycw2k0008jg8m0`, circuit 1: `cy22fne6vek0008rbv8g`, and circuit 2: `cy22wdh9b62g008h80y0`. Result is here:

![](../figures/paper_2025/discriminator_iq_clusters_q109_2025-01-31.png)

# T1

One channel case: `cy5we10rta1g00873a50`. Two channels case: `cy5wyv301rbg008j6grg`. Results are here

![](../figures/paper_2025/t1_q109_one_decay_channel.png)

![](../figures/paper_2025/t1_q109_two_decay_channels.png)

# T2

Ramsey experiment, detuning 1 MHz, `cyfv8xb01rbg008fhvx0`. This can be used to estimate $T_2$. Result is here

![](../figures/paper_2025/ramsey12_q109_cyfv8xb01rbg008fhvx0.png)

Then I tried to observe the peaks caused by dephasing. This one is from `cyfv8na01rbg008fhvw0`. Detuning was 0.1.

![](../figures/paper_2025/ramsey12_q109_cyfv8na01rbg008fhvw0.png)

Then I tried to observe the peaks caused by dephasing. This one is from `cyfq51wcw2k00088wv4g`. Detuning was 0.5.

![](../figures/paper_2025/ramsey12_q109_cyfq51wcw2k00088wv4g.png)

# Coherent amplitude errors

### Experiment ID: `cw0s2fsrxqkg008e2cag`

Amplitude was `0.25136`. No drag, no scaling. Basically uncorrected.

![](../figures/paper_2025/rotation_error_q109_cw0s2fsrxqkg008e2cag.png)

### Experiment ID: `cw0w06rvka8g008b997g`

Amplitude was `0.25136`. WITH drag, $-0.4141$, no scaling.

![](../figures/paper_2025/rotation_error_q109_cw0w06rvka8g008b997g.png)

### Experiment ID: `cw24b0crxqkg008e56j0`

Amplitude was `0.23629` (SCALED). WITH drag, $-0.4141$.

![](../figures/paper_2025/rotation_error_q109_cw24b0crxqkg008e56j0.png)

### Experiment ID: `cw13qsqvka8g008b9vg0`

Amplitude was `0.23629` (SCALED). WITH drag, $-0.4141$.

![](../figures/paper_2025/rotation_error_q109_cw13qsqvka8g008b9vg0.png)

### Experiment ID: `cw0wed14v2e0008sg2gg`

Amplitude was `0.23629` (SCALED). WITH drag, $-0.4141$.

![](../figures/paper_2025/rotation_error_q109_cw0wed14v2e0008sg2gg.png)

### Experiment ID: `cvr07a5zrwzg008axdc0`

Without drag, scaled from without drag

---

### Experiment ID: `cxq97543wrp0008kjp30`

Intentionally adding 1% of over-rotation error.

### Experiment ID: `cxqf2yb4a290008xk0n0` (choose this for uncorrected gate)

Intentionally adding 3% of over-rotation error.

### Experiment ID: `cxqzkex082700083ynxg`

Intentionally adding 5% of over-rotation error.

### Experiment ID: `cxqzqfxwk6yg008hq2k0`

Intentionally adding 7% of over-rotation error

### Experiment ID: `cxqzry34a290008xmaj0`

Intentionally adding 9% of over-rotation error

### Experiment ID: `cxr33044a290008xmh10`

Intentionally adding 11% of over-rotation error

### Experiment ID: `cxr5ydhy1ae0008n19ag`

Intentionally adding 13% of over-rotation error

---

### Experiment ID: `cyf0kfx9b62g008jp5sg`

Used Rabi-calibrated amplitude. Seems like it's underrestimating epsilon. The yielded epsilon is `1.191e-02`. No DRAG correction.

# Ramsey

We need two Ramseys. The first one to measure the $T_2$ time, and the second one to measure the two peaks.

# DRAPE

### *Experiment ID: `cybdjk2cw2k0008kfs10`, `cyf2m287v8tg008hdsx0`

Looks good. The first one is the most convergent among all experiments, I guess. `0.23678929765886286`. The second one resulted from an attempt to re-focus the Bloch vector due to predicted dephasing, but failed. However, it speaks volume about the fact that this SNR can be manipulated. Requires further investigation!

### Experiment ID: `cy699tfnrmz00085kdtg`

Relatively recent one, `0.23557046979865773`. Indicating a different DRAG param but on the 0.5 line. En fait c'est la ligne de base.

### Experiment ID: `cy99xfn7v8tg008fs4e0`

L'experience qui dicte la ligne de base.

### Experiment ID: `cwhvkgy543p00086em8g`

This one probe the 7, 9, 11 range. The deviation is largely reduced. I guess this can be explain by the fact that the $\cos\epsilon$ term grows larger than the random fluctuation term.

### *Experiment ID: `cw64ghtxa9wg008vqy4g`, `cw63e40vwdtg0081kj60`, `cw6n0bhggr6g0087cz80`, `cw0tm9154nq0008x5rdg`

Old ones. Looking good. Intended to be on the paper.

### Experiment ID: `cw6dsf5bhxtg008wbkr0`, `cw6fbkyjyrs0008gj6zg`, `cw9s6e99ezk000815vyg`, `cw9t33wjzdhg008eh20g`, `cw9z24g2802g0081p1c0`

Old ones. These are the same experiments as above (direcly above this cell, cf. `cw6n0bhggr6g0087cz80`), only that it's done at another point in time. Do not converge anymore. But I realize that they short of all shifted to the right, it means that I should have changed something to the experimental parameters...

### Experiment ID: `cvt79qyx1h0g0082q4q0`, `cvtg1bdw07b0008m7ehg`, `cvtjckj709200088jmbg`

Old ones. Not positioning at pi/2, thus not having good resolution.

### Experiment ID: `cw6cg8hvwdtg008knj6g`, `cw6d2ykpcbmg0089dtw0`

Two old ones. The first one `amp_sx12=0.2362`, looks particularly bad. Dunno why. The second one, `amp_sx12=0.2361` looks better, in the sense that that converge near -0.415 (what we estimate to the the good value) and closer to 0.5. Hmmm.

### Experiment ID: `cw61yptxa9wg008a8jb0`

An old one. Amp was `0.25`. This says that the further away you're from the correct amp, the further you're away from 0.5.

### Experiment ID: `cwhtad131we000881mgg`, `cwhvkgy543p00086em8g`

Two relatively more recent experiments. Used 7, 9, 11 repetitions. The second one has a slightly larger amplitude. Indicate that SN ratio is enhanced when increasing repetition.

# APE

### Experiment ID: `cw0sjvk79ws0008z27j0`, `cw0t1qe4v2e0008sfxeg`, `cw0twskjz3x0008j6xx0`, `cw0v84079ws0008z2as0`

W/o DRAG `cw0sjvk79ws0008z27j0` 1-3, `cw0t1qe4v2e0008sfxeg` 5-7, and with DRAG `cw0twskjz3x0008j6xx0` 1-3, `cw0v84079ws0008z2as0` 5-7.

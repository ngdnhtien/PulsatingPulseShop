# Lab log, July 2024 (from `log.ipynb`, 'Qutrit Control Project (QCP24)')

# Qutrit Control Project (QCP24)

## Theoretical Division

### 17th July 2024

- Does a simple theory explaining how different durations perform differently exist?
    - We could always rely on Fourier transform (direction 1).

## Experminental Division

### 17th July 2024

- Data for DRAG calibration using two special points differ drastically. Data at $\phi=0$ has a SNR ratio much better than that at $\phi=\pi$. I don't know why.
- After obtaining DRAG parameter from using the APE sequence,
    - The APE sequence (before DRAG) does align.
    - The RE sequence does not show signs of reduced error (1/4).
- I'm thinking about operating with a different duration. Begining with $\tau=48+8$. It could be just that a good rabi oscillation cosine plot does not equal to good duration.


### 23th July 2024

- Do the fitting for all Rabi oscillations (with different durations) again.
    - Tryna understand how `average` and `single` signals are intergrated (or processed)
- I figured the metric for "how good Rabi oscillation" should fit, experimentally
    - The trick is to look at the plot of variance: either the real part, or assuming a 2D normal distribution
    - When sweeping over the range of 100 amplitudes, a 2D normal distribution should have two points with minimal variance. The two points correspond to the |1> and the |2> state.
    - This way, a good duration corresponds to the case when the second variance reaches the minimum of mimimum.
    - Also, this is a very good way of "knowing" exactly whether it is a |2> state. 
    - This is because, once you have a state that is an eigenstate of the "Pauli Z12", you have a 1 on 1 chance of measuring that state. 

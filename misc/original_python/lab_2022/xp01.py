### General pulse instruction ###

with pulse.build(backend=backend) as inst_x_pi_01:
    drive_chan = pulse.drive_channel(qubit)
    pulse.play(pulse.Gaussian(duration=drive_duration_01,
                              amp=drive_amplitude_01,
                              sigma=drive_sigma_01), drive_chan)
                              
inst_x_pi_01.draw()

### ibmq_oslo ###

"""
    The following parameteres were last 
    updated on 7th September, 2022
    + Qubit: 0
    + Backend: ibm_oslo
    + Pulse instruction: Pi pulse on subspace (0-1)
"""

# Pulse parameters
drive_duration_01 = 544
drive_sigma_01 = 67
drive_amplitude_01 = 0.07902104192057431


### ibmq_manila ###

"""The following parameteres were last updated on 19th September, 2022
   This is the ibmq_manila backend, qubit 0, on subspace (0-1)"""

# Pulse parameters (slow gate)
drive_frequency_01 = 4962317255.07658
drive_duration_01 = 544
drive_sigma_01 = 67
drive_amplitude_01 = 0.09281388317671437

# Pulse parameters (fast gate)
drive_frequency_01 = 4962131445.5726
drive_duration_01 = 160
drive_sigma_01 = 40
drive_amplitude_01 = 0.2127889627295832

"""The following parameteres were last updated on 13th October, 2022
   This is the ibm_oslo backend, qubit 0, on subspace (0-1)"""
drive_duration_01 = 320
drive_sigma_01 = 80
drive_amplitude_01 = 0.07513041041956571


### General pulse instruction ###

with pulse.build(backend=backend) as inst_x_fullpi_12:
    drive_chan = pulse.drive_channel(qubit)
    pulse.play(pulse.Gaussian(duration=drive_duration_12,
                              amp=drive_amplitude_12,
                              sigma=drive_sigma_12), drive_chan)
                              
inst_x_fullpi_12.draw()

### ibmq_manila ###

""" The following parameteres were last updated on 14rd September, 2022
    This is the ibmq_manila backend, qubit 0, on subspace (1-2) """

# Pulse parameters
drive_frequency_12 = 4618781329.919704
drive_duration_01 = 160
drive_sigma_01 = 40
drive_amplitude_12 = 0.17306617215735373

"""The following parameteres were last updated on 13th October, 2022
   This is the ibm_oslo backend, qubit 0, on subspace (0-1)"""
drive_duration_01 = 320
drive_sigma_01 = 80
drive_amplitude_01 = 0.07077182615095635

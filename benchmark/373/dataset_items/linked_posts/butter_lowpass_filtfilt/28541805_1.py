import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filtfilt(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = filtfilt(b, a, data)
    return y

data = np.loadtxt('data.dat', skiprows=2, delimiter=',', unpack=True).transpose()
time = data[:,0]
pressure = data[:,1]
cutoff = 1500
fs = 50000
pressure_smooth = butter_lowpass_filtfilt(pressure, cutoff, fs)

figure_pressure_trace = plt.figure()
figure_pressure_trace.clf()
plot_P_vs_t = plt.subplot(111)
plot_P_vs_t.plot(time, pressure, 'r', linewidth=1.0)
plot_P_vs_t.plot(time, pressure_smooth, 'b', linewidth=1.0)
plt.show()
plt.close()

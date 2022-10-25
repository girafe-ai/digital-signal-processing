import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import lfilter, butter

# Create input signal
t = 2 * np.pi * np.linspace(-1, 1, 500)
x = np.sin(0.25 * t * t) + 0.95 * np.sin(2.0 * t)

# Add some white noise
np.random.seed(1)
xn = x + np.random.randn(len(t))

# 3-order lowpass butterworth filter
b, a = butter(3, 0.2)
z = lfilter(b, a, xn)

wn = [0.01, 0.05, 0.1, 0.2]

# Calculate IIR filter
zz = np.zeros((t.size, 4))
for i in range(4):
    b, a = butter(3, wn[i])
    zz[:, i] = lfilter(b, a, xn)

# Plot results
plt.figure(figsize=(32, 16), dpi=80)
for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.plot(t, xn, 'C0--', linewidth=1.5)
    plt.plot(t, zz[:, i], 'C1', linewidth=2.5)
    plt.xlim([-2 * np.pi, 2 * np.pi])
    plt.grid(True)
    plt.legend(('Signal', 'Filtered, wn = {}'.format(wn[i])), loc='lower left')
plt.show()

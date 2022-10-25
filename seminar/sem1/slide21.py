import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft

N = 128
# Time vector
t = np.linspace(0, 1, N)

# Amplitudes and freqs
f1, f2, f3 = 2, 7, 12
A1, A2, A3 = 5, 1, 3

# Signal
x = A1 * np.cos(2*np.pi*f1*t) + A2 * np.cos(2*np.pi*f2*t) + A3 * np.cos(2*np.pi*f3*t)

# Calculate FFT
X = fft(x)
X = 2*np.abs(X) / N

# Plot results
fig = plt.figure(figsize=(24, 8), dpi=80)
# Time: signal
plt.subplot(1, 2, 1)
plt.title('Signal')
plt.stem(x, use_line_collection=True, basefmt='C0')
plt.xlim([0, N-1])
plt.xlabel('samples')
plt.grid()

# Freq: Spectrum
plt.subplot(1, 2, 2)
plt.title('Spectrum')
plt.stem(X, use_line_collection=True, basefmt='C0')
plt.xlim([0, N//2-1])
plt.xlabel('frequency')
plt.grid()
plt.tight_layout()
plt.show()
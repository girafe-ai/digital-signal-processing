import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft

N = 9    # Signal period
M = 4    # Number of repeats

# Signal
x = np.zeros(N)
x[0:3] = 1
y = np.tile(x, M)

# Forward FFT
NFFT = 1024
xFFT = fft(y, NFFT)
# Magnitude spectrum
yA = np.abs(xFFT)
yA /= np.max(yA)
# Phase spectrum
yF = np.angle(xFFT)

# FFT for input signal
xFFT = fft(x, NFFT)
# Magnitude spectrum
xA = np.abs(xFFT)
xA /= np.max(xA)

# FFT for repeats
xFFT = fft(x, NFFT // N)
# Magnitude spectrum
xM = np.abs(xFFT)
xM /= np.max(xM)
xM = np.tile(xM, N)
# List of signals
xT = [y, yA]
lst_title = ['Signal', 'Spectrum', 'Phase']

# Plot results
fig = plt.figure(figsize=(24, 12), dpi=80)
for i, sig in enumerate(xT):
    plt.subplot(2, 1, int(2 ** i))
    plt.ylabel('Level')
    plt.title(lst_title[i])
    if i == 0:
        plt.stem(sig, use_line_collection=True, basefmt='C0')
        plt.xlabel('Time samples')
        plt.ylim([0, 1.5])
        plt.xlim([-0.5, N * M - 0.5])
    else:

        plt.plot(sig, '-', linewidth=2.5, label='Result Spectrum y(t)')
        plt.plot(xA, '--', linewidth=1.5, label='Input Spectrum x(t)')
        plt.plot(xM, '-.', linewidth=1.5, label='Repeats by M = %d' % M)
        plt.xlabel('Freq samples')
        plt.xlim([0, NFFT - 1])
        plt.legend(loc='upper right')
    plt.grid()
plt.tight_layout()
plt.show()
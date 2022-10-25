import matplotlib.pyplot as plt
import numpy as np

n = 6
# time vector
t = np.linspace(-n, n - 1, 2 * n)

# Delta function
xd = np.zeros(2 * n)
xd[n] = 1

# Heaviside function
xh = np.heaviside(t, 1)

# Combine them together
xs = [xh, xd]

# Plot results
fig = plt.figure(figsize=(24, 6), dpi=80)
for i, sig in enumerate(xs):
    plt.subplot(1, 2, i + 1)
    plt.stem(t, sig, linefmt='C3', markerfmt='D', use_line_collection=True)
    plt.ylabel('Amplitude')
    plt.xlabel('Samples')
    plt.xticks(t)
    plt.xlim([np.min(t) + 1, np.max(t)])
    plt.grid(True)
plt.tight_layout()
plt.show()

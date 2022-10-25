import matplotlib.pyplot as plt
import numpy as np

N = 4
nk = np.array([i * j for i in range(N) for j in range(N)]).reshape(N, N)

# Twiddle
Wnk = np.round(np.exp(-2j * np.pi * nk / N), 3)
print(Wnk)

N = 8
nk = np.array([i * j for i in range(N) for j in range(N)]).reshape(N, N)

# Twiddle
Wnk = np.round(np.exp(-2j * np.pi * nk / N), 3)
print(Wnk)

fig = plt.figure(figsize=(24, 8), dpi=80)

plt.subplot(1, 2, 1)
for i in range(N):
    plt.plot(np.real(Wnk[i, :]), '--o', linewidth=1.15)
plt.grid(True)
plt.subplot(1, 2, 2)
for i in range(N):
    plt.plot(np.imag(Wnk[i, :]), '--o', linewidth=1.15)
plt.grid(True)
plt.tight_layout()
plt.show()

N = 16
nk = np.array([i * j for i in range(N) for j in range(N)]).reshape(N, N)

# Twiddle
Wnk = np.round(np.exp(-2j * np.pi * nk / N), 5)

fig = plt.figure(figsize=(28, 16), dpi=80)
for i in range(N):
    plt.subplot(N // 4, 4, i + 1)
    plt.plot(np.real(Wnk[i, :]), '--o', linewidth=0.5, label='W{}'.format(i))
    plt.grid(True)
    plt.legend(loc='upper right')
plt.tight_layout()
plt.show()

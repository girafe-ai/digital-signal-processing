import matplotlib.pyplot as plt
import numpy as np

# Digital signal
xt = np.array([2, 1, -2, 0, 2, 3, 1, -1])
# Time vector
t = np.linspace(0, xt.size-1, xt.size, endpoint=True)

# Plot figure
fig = plt.figure(figsize=(16, 6), dpi=80)
plt.title('Digital signal')
plt.stem(t, xt, linefmt='C3', markerfmt='D', use_line_collection=True)
plt.xticks(t)
plt.xlim([np.min(t)-0.2, np.max(t)+0.2])
plt.grid(True)
plt.show()
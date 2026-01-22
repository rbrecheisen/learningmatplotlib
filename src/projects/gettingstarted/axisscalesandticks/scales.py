import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(100)
fig, axs = plt.subplots(1, 2, figsize=(5, 2.7), layout='constrained')
xdata = np.arange(len(data))
ydata = 10**data
axs[0].plot(xdata, ydata)
axs[1].set_yscale('log')
axs[1].plot(xdata, ydata)
plt.show()
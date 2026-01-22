import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(100)
fig, axs = plt.subplots(1, 2, figsize=(5, 2.7), layout='constrained')
xdata = np.arange(len(data))
ydata = data
axs[0].plot(xdata, ydata)
axs[0].set_title('Automatic ticks')

axs[1].plot(xdata, ydata)
axs[1].set_xticks(np.arange(0, 100, 30), ['zero', '30', 'sixty', '90'])
axs[1].set_yticks([-1.5, 0, 1.5])
axs[1].set_title('Manual ticks')

plt.show()
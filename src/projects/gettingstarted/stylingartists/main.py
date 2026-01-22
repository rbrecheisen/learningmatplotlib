import matplotlib.pyplot as plt
import numpy as np

data1, data2 = np.random.randn(2, 100)
x = np.arange(len(data1))
fig, ax = plt.subplots(figsize=(5, 2.7))
ax.plot(x, np.cumsum(data1), color='blue', linewidth=3, linestyle='--')
l = ax.plot(x, np.cumsum(data2), color='orange', linewidth=2) # Returns list of objects
l[0].set_linestyle(':') # Set line style after the fact
plt.show()
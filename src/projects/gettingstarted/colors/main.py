import matplotlib.pyplot as plt
import numpy as np

data1, data2 = np.random.randn(2, 100)
fig, ax = plt.subplots(figsize=(5, 2.7))
# https://matplotlib.org/stable/users/explain/colors/colors.html#colors-def
# Color 'C0' is CN color specification. Color 'k' refers to black.
ax.scatter(data1, data2, s=50, facecolor='C0', edgecolor='k')
plt.show()
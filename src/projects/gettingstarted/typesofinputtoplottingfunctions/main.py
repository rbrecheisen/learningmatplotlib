import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
data = {
    'a': np.arange(50),
    'c': np.random.randint(0, 50, 50),
    'd': np.random.randn(50),
}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
# Create scatter plot. The argument values 'a', 'b', 'c' and 'd' refer to the keys
# in 'data'. The argument 'c=' sets the color of the points. The argument 's=' sets
# the point size.
ax.scatter('a', 'b', c='c', s='d', data=data)
ax.set_xlabel('entry a')
ax.set_ylabel('entry b')
plt.show()
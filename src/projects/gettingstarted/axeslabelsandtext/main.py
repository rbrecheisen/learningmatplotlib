import matplotlib.pyplot as plt
import numpy as np

mu, sigma = 115, 15
x = mu + sigma * np.random.randn(10000)
fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
n, bins, patches = ax.hist(x, 50, density=True, facecolor='C0', alpha=0.75)
ax.set_xlabel('Length [cm]')
ax.set_ylabel('Probability')
ax.set_title('Aardvark lengths\n (not really)')
# Added LaTeX formatted text. Prepend string with 'r' to handle as raw string
# and not interpret backslashes as Python escape characters
ax.text(75, .025, r'$\mu=115,\ \sigma=15$')
ax.axis([55, 175, 0, 0.03])
ax.grid(True)
plt.show()
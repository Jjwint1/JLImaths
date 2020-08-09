import numpy as np
import matplotlib.pyplot as plt
import math

x = np.linspace(0, 10)

g = lambda x: 1 - np.exp(-x)

plt.plot(x, g(x), '-', lw=1, color="#2D0000")
plt.xlabel(r'$x$')
plt.ylabel(r'$g(x)$')
plt.savefig('../../figures/4_Functions/QQ3d.png', dpi=600)
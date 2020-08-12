import numpy as np
import matplotlib.pyplot as plt

n = np.linspace(0, 15, 150000)

y = lambda n: 60*n - (1/5)*n**3

plt.plot(n, y(n), '-', lw=1, color="#2D0000")
plt.xlabel(r'$n$')
plt.ylabel(r'$y(n)$')
plt.savefig('../../figures/5_Differentiation/LQ1e.png', dpi=600)
plt.close()
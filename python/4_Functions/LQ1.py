import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 400)
t = np.linspace(0, 12)

supply = lambda q: q/50

demand = lambda q: 1200 / (q+100)

tax = lambda q: 3

T = lambda t: 1200*t/(1+t) - 100*t

plt.plot(x, supply(x), '-', lw=1, color="#2D0000", label=r'$p^s$')
plt.plot(x, demand(x), '-', lw=1, color="#002147", label=r'$p^d$')
plt.xlabel(r'q')
plt.ylabel(r'p')
plt.legend()
plt.annotate(xy=[200, 4], xytext=[150, 6], s='Equilibrium: '+r'$(200, 4)$', arrowprops={"arrowstyle": '-'})
plt.savefig('../../figures/4_Functions/LQ1f.png', dpi=600)
plt.close()
plt.plot()
plt.plot(x, supply(x), '-', lw=1, color="#2D0000", label=r'$p^s$')
plt.plot(x, [3 for i in range(len(x))], lw=1, color="#2D0000", label=r'$p^s_{t}$')
plt.plot(x, demand(x), '-', lw=1, color="#002147", label=r'$p^d$')
plt.xlabel(r'q')
plt.ylabel(r'p')
plt.legend()
plt.savefig('../../figures/4_Functions/LQ1g.png', dpi=600)
plt.close()
plt.plot(t, T(t), '-', lw=1, color="#2D0000")
plt.xlabel(r't')
plt.ylabel(r'T')
plt.savefig('../../figures/4_Functions/LQ1i.png', dpi=600)

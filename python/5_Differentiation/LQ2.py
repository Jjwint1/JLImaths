import numpy as np
import matplotlib.pyplot as plt

q = np.linspace(0, 150, 150000)

Pi = lambda q: 15*q - (1/10)*q**2

plt.plot(q, Pi(q), '-', lw=1, color="#2D0000")
plt.xlabel(r'$p$')
plt.ylabel(r'$\Pi(q)$')
plt.savefig('../../figures/5_Differentiation/LQ2f.png', dpi=600)
plt.close()


line = np.linspace(0, 600, 600)
law = [80 for i in range(len(line))]


plt.plot(q, Pi(q), '-', lw=1, color="#2D0000")
plt.plot(law, line, '-', lw=1, color="#002147")
plt.plot()
plt.xlabel(r'$p$')
plt.ylabel(r'$\Pi(q)$')
plt.annotate(xy=[80, 0], xytext=[90, 10], s=r'$q=80$', arrowprops = {"arrowstyle": '-'})
plt.savefig('../../figures/5_Differentiation/LQ2g.png', dpi=600)
plt.close()
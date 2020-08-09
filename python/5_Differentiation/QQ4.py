import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 4)

y = lambda x: 3*x - x**2 + 4


plt.plot(x, y(x), '-', lw=1, color="#2D0000")
plt.annotate(xy=[3/2, 25/4], xytext=[3/2, 5], s=r'$\left(\frac{3}{2}, \frac{25}{4}\right)$', arrowprops={"arrowstyle": '-'})
plt.xlabel(r'$x$')
plt.ylabel(r'$y(x)$')
plt.savefig('../../figures/5_Differentiation/QQ4a.png', dpi=600)
plt.close()


x = np.linspace(0, 30, 300000)

g = lambda x: 6*x**(1/2)-x

plt.plot(x, g(x), '-', lw=1, color="#2D0000")
plt.annotate(xy=[9, 9], xytext=[9, 8], s=r'$\left(9, 9\right)$', arrowprops={"arrowstyle": '-'})
plt.xlabel(r'$x$')
plt.ylabel(r'$g(x)$')
plt.savefig('../../figures/5_Differentiation/QQ4b.png', dpi=600)
plt.close()


x = np.linspace(-1, 4, 50000)

f = lambda x: x**4 - 8*x**3 + 18*x**2 - 5

plt.plot(x, f(x), '-', lw=1, color="#2D0000")
plt.annotate(xy=[0, -5], xytext=[-0.2, -2], s=r'$\left(0, -5\right)$', arrowprops={"arrowstyle": '-'})
plt.annotate(xy=[3, 22], xytext=[3, 18], s=r'$\left(3, 22\right)$', arrowprops={"arrowstyle": '-'})
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.savefig('../../figures/5_Differentiation/QQ4c.png', dpi=600)
plt.close()
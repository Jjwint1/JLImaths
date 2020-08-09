import numpy as np
import matplotlib.pyplot as plt

Q = np.linspace(0, 10, 10000)

MC = lambda Q: (1+(5/2)*Q**(3/2))

plt.plot(Q, MC(Q), '-', lw=1, color="#2D0000")
plt.xlabel(r'$Q$')
plt.ylabel(r'$MC(Q)$')
plt.savefig('../../figures/5_Differentiation/QQ5.png', dpi=600)
plt.close()
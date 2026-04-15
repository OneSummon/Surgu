import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()
x = np.linspace(0, 10, 50)
y1 = x
y2 = x**2

fig, axes = plt.subplots(2, 1, figsize=(9, 9))
fig.suptitle('Зависимости: y1 = x, y2 = x^2')

sns.lineplot(x=x, y=y1, ax=axes[0])
axes[0].set_ylabel('y1', fontsize=14)
axes[0].grid(True)

sns.lineplot(x=x, y=y2, ax=axes[1])
axes[1].set_xlabel('x', fontsize=14)
axes[1].set_ylabel('y2', fontsize=14)
axes[1].grid(True)

plt.show()
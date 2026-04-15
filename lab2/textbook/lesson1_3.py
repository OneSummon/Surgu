import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()
x = np.linspace(0, 10, 50)
y = x

ax = sns.lineplot(x=x, y=y)
ax.set_title('Линейная зависимость y = x')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.grid(True)
plt.show()
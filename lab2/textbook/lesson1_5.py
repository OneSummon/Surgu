import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

sns.set_theme()
x = np.linspace(0, 10, 50)
y1 = x
y2 = x**2

df = pd.DataFrame({'x': np.concatenate([x, x]),
                   'y': np.concatenate([y1, y2]),
                   'line': ['y1=x']*50 + ['y2=x^2']*50})

ax = sns.lineplot(data=df, x='x', y='y', hue='line')
ax.set_title('Зависимости: y1 = x, y2 = x^2')
ax.set_xlabel('x')
ax.set_ylabel('y1, y2')
plt.show()
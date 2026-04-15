import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set_theme()

np.random.seed(123)
vals = np.random.randint(10, size=(7, 7))

fig, ax = plt.subplots()
sns.heatmap(vals, ax=ax, cmap='viridis', cbar=True,
            cbar_kws={
                'orientation': 'horizontal',
                'shrink': 0.9,
                'extend': 'max',
                'extendfrac': 0.2,
                'extendrect': False,
                'drawedges': False
            })

plt.show()
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set_theme()

vals = np.random.randint(10, size=(7, 7))

fig, ax = plt.subplots()
sns.heatmap(vals, ax=ax, cmap='viridis', cbar=True)

plt.show()
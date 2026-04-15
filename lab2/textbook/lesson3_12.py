import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()
weight = ['light', 'regular', 'bold']
fig, axes = plt.subplots(1, 3, figsize=(12, 4))

for i, (ax, lc) in enumerate(zip(axes, ['left', 'center', 'right'])):
    ax.set_title(label=lc, loc=lc, fontsize=12 + i * 5,
                 fontweight=weight[i], pad=10 + i * 15)

plt.show()
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()
locs = ['best', 'upper right', 'upper left', 'lower left',
        'lower right', 'right', 'center left', 'center right',
        'lower center', 'upper center', 'center']

x = [1, 5, 10, 15, 20]
y1 = [1, 7, 3, 5, 11]
y2 = [4, 3, 1, 8, 12]

fig, axes = plt.subplots(3, 4, figsize=(12, 12))

for i in range(3):
    for j in range(4):
        idx = i * 4 + j
        if idx < 11:
            ax = axes[i, j]
            sns.lineplot(x=x, y=y1, marker='o', linestyle='-',  color='red',   label='line 1', ax=ax)
            sns.lineplot(x=x, y=y2, marker='o', linestyle='-.', color='green', label='line 2', ax=ax)
            ax.set_title(locs[idx])
            ax.legend(loc=locs[idx])
        else:
            axes[i, j].set_visible(False)

plt.tight_layout()
plt.show()
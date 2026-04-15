import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

sns.set_theme()
x = [1, 2, 3, 4, 5]
y1 = [9, 4, 2, 4, 9]
y2 = [1, 7, 6, 3, 5]

fg = plt.figure(figsize=(7, 3), constrained_layout=True)
gs = gridspec.GridSpec(ncols=2, nrows=1, figure=fg)
ax1 = fg.add_subplot(gs[0, 0])
sns.lineplot(x=x, y=y1, ax=ax1)
ax2 = fg.add_subplot(gs[0, 1])
sns.lineplot(x=x, y=y2, ax=ax2)
plt.show()
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()
x = [1, 2, 3, 4, 5]
y1 = [9, 4, 2, 4, 9]
y2 = [1, 7, 6, 3, 5]
y3 = [-7, -4, 2, -4, -7]

fg = plt.figure(figsize=(9, 4), constrained_layout=True)
gs = fg.add_gridspec(2, 2)
ax1 = fg.add_subplot(gs[0, :])
sns.lineplot(x=x, y=y2, ax=ax1)
ax2 = fg.add_subplot(gs[1, 0])
sns.lineplot(x=x, y=y1, ax=ax2)
ax3 = fg.add_subplot(gs[1, 1])
sns.lineplot(x=x, y=y3, ax=ax3)
plt.show()
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()

bbox_properties = dict(
    boxstyle='rarrow, pad=0.3',
    ec='g',
    fc='r',
    ls='-',
    lw=3
)

fig, ax = plt.subplots()
sns.lineplot(x=range(0, 10), y=range(0, 10), ax=ax)
ax.set_title('Title', fontsize=17, bbox=bbox_properties, position=(0.5, 0.85))

plt.show()
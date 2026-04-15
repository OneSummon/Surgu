import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()
ax = sns.lineplot(x=list(range(10)), y=list(range(10)))
bbox_properties = dict(boxstyle='darrow,pad=0.3', ec='k', fc='y', ls='-', lw=3)
ax.text(2, 7, 'HELLO!', fontsize=15, bbox=bbox_properties)
plt.show()
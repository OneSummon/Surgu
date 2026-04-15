import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()
ax = sns.lineplot(x=list(range(10)), y=list(range(10)))
ax.text(0, 7, 'HELLO!', fontsize=15)
plt.show()
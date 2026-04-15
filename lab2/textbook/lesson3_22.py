import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()

fig, ax = plt.subplots()
sns.lineplot(x=range(0, 10), y=range(0, 10), ax=ax)
ax.set_title('Title', fontsize=17, position=(0.7, 0.2), rotation='vertical')

plt.show()
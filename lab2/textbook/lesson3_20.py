import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()
ax = sns.lineplot(x=list(range(10)), y=list(range(10)))
ax.set_title('Title', alpha=0.5, color='r', fontsize=18,
             fontstyle='italic', fontweight='bold', linespacing=10)
plt.show()
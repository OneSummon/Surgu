import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()
x = list(range(-5, 6))
y = [i**2 for i in x]

ax = sns.lineplot(x=x, y=y)
ax.annotate('min', xy=(0, 0), xycoords='data', xytext=(0, 10),
            textcoords='data', arrowprops=dict(facecolor='g'))
plt.show()
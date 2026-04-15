import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()
x = [1, 5, 10, 15, 20]
y = [1, 7, 3, 5, 11]
sns.lineplot(x=x, y=y, linestyle='--')
plt.show()
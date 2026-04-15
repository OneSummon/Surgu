import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()
x = [1, 5, 10, 15, 20]
y1 = [1, 7, 3, 5, 11]
y2 = [4, 3, 1, 8, 12]

sns.lineplot(x=x, y=y1, marker='o', linestyle='-',  color='red',   label='L1')
sns.lineplot(x=x, y=y2, marker='o', linestyle='-.', color='green', label='L2')
plt.legend()
plt.show()
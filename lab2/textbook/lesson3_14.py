import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()
x = list(range(10))
y = [i * 2 for i in range(10)]

ax = sns.lineplot(x=x, y=y)
ax.set_xlabel('Ось X\nНезависимая величина', fontsize=14, fontweight='bold')
ax.set_ylabel('Ось Y\nЗависимая величина', fontsize=14, fontweight='bold')
plt.show()
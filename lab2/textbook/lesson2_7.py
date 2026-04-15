import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()
x = [1, 5, 10, 15, 20]
y1 = [1, 7, 3, 5, 11]
y2 = [i*1.2 + 1 for i in y1]
y3 = [i*1.2 + 1 for i in y2]
y4 = [i*1.2 + 1 for i in y3]

palette = sns.color_palette()
sns.lineplot(x=x, y=y1, linestyle='-',  color=palette[0])
sns.lineplot(x=x, y=y2, linestyle='--', color=palette[1])
sns.lineplot(x=x, y=y3, linestyle='-.',color=palette[2])
sns.lineplot(x=x, y=y4, linestyle=':', color=palette[3])
plt.show()
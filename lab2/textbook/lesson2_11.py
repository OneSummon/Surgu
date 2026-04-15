import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()
x = [1, 5, 10, 15, 20]
y1 = [1, 7, 3, 5, 11]
y2 = [i*1.2 + 1 for i in y1]
y3 = [i*1.2 + 1 for i in y2]
y4 = [i*1.2 + 1 for i in y3]

fig, axs = plt.subplots(2, 2, figsize=(12, 7))
sns.lineplot(x=x, y=y1, linestyle='-',  ax=axs[0, 0])
sns.lineplot(x=x, y=y2, linestyle='--', ax=axs[0, 1])
sns.lineplot(x=x, y=y3, linestyle='-.',ax=axs[1, 0])
sns.lineplot(x=x, y=y4, linestyle=':', ax=axs[1, 1])

plt.show()
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

sns.set_theme()
x = [1, 5, 10, 15, 20]
y1 = [1, 7, 3, 5, 11]
y2 = [4, 3, 1, 8, 12]

line1 = sns.lineplot(x=x, y=y1, marker='o', linestyle='-',  color='blue',    label='L1')
line2 = sns.lineplot(x=x, y=y2, marker='o', linestyle='-.', color='magenta', label='L2')

handles, labels = plt.gca().get_legend_handles_labels()
plt.legend([handles[1], handles[0]], ['L2', 'L1'])
plt.show()
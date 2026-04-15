import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()
x = [1, 5, 10, 15, 20]
y = [1, 7, 3, 5, 11]

ax = sns.lineplot(x=x, y=y, label='steel price')
ax.set_title('Chart price', fontsize=15)
ax.set_xlabel('Day', fontsize=12, color='blue')
ax.set_ylabel('Price', fontsize=12, color='blue')
ax.legend()
ax.grid(True)
ax.text(15, 4, 'grow up!')
plt.show()
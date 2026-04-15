import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()
fruits = ['apple', 'peach', 'orange', 'bannana', 'melon']
counts = [34, 25, 43, 31, 17]

ax = sns.barplot(x=fruits, y=counts)
ax.set_title('Fruits!')
ax.set_xlabel('Fruit')
ax.set_ylabel('Count')
plt.show()
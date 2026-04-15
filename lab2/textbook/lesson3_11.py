import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
fig.suptitle('suptitle')
plt.figtext(0.5, -0.1, 'figtext')

axes[0].set_title('title')
axes[0].set_xlabel('xlabel')
axes[0].set_ylabel('ylabel')
axes[0].text(0.2, 0.2, 'text')
axes[0].annotate('annotate', xy=(0.2, 0.4), xytext=(0.6, 0.7),
                 arrowprops=dict(facecolor='black', shrink=0.05))

axes[1].set_title('title')
axes[1].set_xlabel('xlabel')
axes[1].set_ylabel('ylabel')
axes[1].text(0.5, 0.5, 'text')

plt.show()
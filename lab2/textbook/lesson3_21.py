import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

sns.set_theme()
ax = sns.lineplot(x=list(range(10)), y=list(range(10)))
ax.set_title('Title', fontproperties=FontProperties(
    family='monospace', style='italic', weight='heavy', size=15))
plt.show()
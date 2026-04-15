import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()
fg = plt.figure(figsize=(5, 5), constrained_layout=True)
widths = [1, 3]
heights = [2, 0.7]
gs = fg.add_gridspec(ncols=2, nrows=2, width_ratios=widths, height_ratios=heights)

for (i, j), title in [
    ((0, 0), 'w:1, h:2'),
    ((0, 1), 'w:3, h:2'),
    ((1, 0), 'w:1, h:0.7'),
    ((1, 1), 'w:3, h:0.7'),
]:
    ax = fg.add_subplot(gs[i, j])
    ax.set_title(title)

plt.show()
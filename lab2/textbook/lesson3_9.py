import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()
fg = plt.figure(figsize=(9, 9), constrained_layout=True)
gs = fg.add_gridspec(5, 5)

for spec, title in [
    (gs[0, :3],   'gs[0, :3]'),
    (gs[0, 3:],   'gs[0, 3:]'),
    (gs[1:, 0],   'gs[1:, 0]'),
    (gs[1:, 1],   'gs[1:, 1]'),
    (gs[1, 2:],   'gs[1, 2:]'),
    (gs[2:4, 2],  'gs[2:4, 2]'),
    (gs[2:4, 3:], 'gs[2:4, 3:]'),
    (gs[4, 3:],   'gs[4, 3:]'),
]:
    ax = fg.add_subplot(spec)
    ax.set_title(title)

plt.show()
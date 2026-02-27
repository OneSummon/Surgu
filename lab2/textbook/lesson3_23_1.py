import matplotlib.pyplot as plt
import numpy as np

np.random.seed(123)
vals = np.random.randint(10, size=(7, 7))
plt.pcolor(vals)

plt.show()
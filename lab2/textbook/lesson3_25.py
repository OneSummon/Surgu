import matplotlib.pyplot as plt
import numpy as np

vals = np.random.randint(10, size=(7, 7))
plt.pcolor(vals, cmap=plt.get_cmap('viridis', 11) )
plt.colorbar()

plt.show()
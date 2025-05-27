import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# prepare some coordinates
x, y, z = np.indices((8, 8, 8))

# draw cuboids in top left and bottom right corners
cube1 = (x < 3) & (y < 3) & (z < 3)
cube2 = (x >= 5) & ()
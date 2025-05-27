import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# prepare some coordinates
x, y, z = np.indices((8, 8, 8))

# draw cuboids in top left and bottom right corners
cube1 = (x < 3) & (y < 3) & (z < 3)
cube2 = (x >= 5) & (y >= 5) & (z >= 5)

# combine objects into a single boolean array
voxelarray = cube1 | cube2

# plot
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.voxels(voxelarray, edgecolor='k')

ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])

plt.show()
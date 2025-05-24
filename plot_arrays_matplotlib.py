import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()          
ax.plot([1, 2, 3, 4], [1, 4, 2, 3]) 
plt.show()

fig = plt.figure()
fig,ax = plt.subplots()
fig,axs = plt.subplots(2,2)

fig, axs = plt.subplot_mosaic([['left', 'right_top'],
                               ['left', 'right_bottom']])
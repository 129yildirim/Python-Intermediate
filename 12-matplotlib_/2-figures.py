import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 9, 20)
y = x**3
z = x**2
#figure = plt.figure()

#-------------1-------------------------
"""
#axes = figure.add_axes([0.2, 0.2, 0.8, 0.8])
axes_cube = figure.add_axes([0.2, 0.1, 0.7, 0.8])
axes_cube.plot(x, y, 'o--b')
axes_cube.set_xlabel('X Axis')
axes_cube.set_ylabel('Y Axis')
axes_cube.set_title('Cube')

axes_square = figure.add_axes([0.3, 0.6, 0.25, 0.25])
axes_square.plot(x, z, 'g')
axes_square.set_xlabel('x axis')
axes_square.set_ylabel('y axis')
axes_square.set_title('square')

plt.show()
"""

#-----------------2------------------
"""
axes = figure.add_axes([0, 0, 1, 1])
axes.plot(x, z, label="Square")
axes.plot(x, y, label="Cube")
axes.legend(loc=4)
plt.show()
"""

#fig, axes = plt.subplots(nrows=2, ncols=1)
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(4, 4))

axes[0].plot(x, y)
axes[0].set_title('Cube')
axes[1].plot(x, z)
axes[1].set_title('Square')

plt.tight_layout()
#fig.savefig('figure1.png')
fig.savefig('figure2.pdf')

plt.show()
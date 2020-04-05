# 5. Задание (в программе)
# Нарисуйте трехмерный график двух любых поверхностей второго порядка.


import numpy as np
import matplotlib.pyplot as plot
from matplotlib import cm

fig = plot.figure()
ax = fig.gca(projection='3d')
X = np.arange(-10, 10, 1)
Y = np.arange(-10, 10, 1)
X, Y = np.meshgrid(X, Y)

Z = 1-3*X**2+2*X*Y-Y**2

xcolors = X - min(X.flat)
xcolors = xcolors/max(xcolors.flat)

surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, facecolors=cm.hot(xcolors), linewidth=1)


fig1 = plot.figure()
ax = fig1.gca(projection='3d')
X1 = np.arange(-10, 10, 1)
Y1 = np.arange(-10, 10, 1)
X1, Y1 = np.meshgrid(X1, Y1)

Z1 = X1**2/3-Y1**2/2

surf1 = ax.plot_surface(X1, Y1, Z1, rstride=1, cstride=1, facecolors=cm.hot(xcolors), linewidth=1)

plot.show()


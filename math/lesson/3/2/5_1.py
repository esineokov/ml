# 5. Задание (в программе)
# Нарисуйте трехмерный график двух параллельных плоскостей.

import random

import numpy as np
import matplotlib.pyplot as plot

a, b, c, d = [random.randint(1, 5) for i in range(4)]
d2 = d+10

x = np.linspace(-10, 10, 20)
y = np.linspace(-10, 10, 20)

X, Y = np.meshgrid(x, y)
Z = (d - a*X - b*Y) / c
Z2 = (d2 - a*X - b*Y) / c

fig = plot.figure()
ax = fig.gca(projection='3d')

ax.plot_surface(X, Y, Z)
ax.plot_surface(X, Y, Z2)

plot.show()

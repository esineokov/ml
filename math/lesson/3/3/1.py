# 1. Задание (в программе)
# Нарисуйте график функции:
# y(x) = k∙cos(x – a) + b
# для некоторых (2-3 различных) значений параметров k, a, b

import matplotlib.pyplot as plot
import numpy as np

k, a, b = 1, 2, 3
k1, a1, b1 = 3, 4, 5
k2, a2, b2 = 6, 7, 8

x = np.arange(0, 10, 0.1)
y = k*np.cos(x-a) + b
y1 = k1*np.cos(x-a1) + b1
y2 = k2*np.cos(x-a2) + b2

plot.plot(x, y)
plot.plot(x, y1)
plot.plot(x, y2)
plot.show()


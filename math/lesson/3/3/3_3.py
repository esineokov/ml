# 3. Задание (в программе)
# Напишите код, который будет рисовать график отрезка прямой линии в полярных координатах.

import numpy as np
import matplotlib.pyplot as plot

plot.axes(projection='polar')

R = np.arange(0, 10, 0.01)
for r in R:
    plot.polar(90, r, '.')

plot.show()

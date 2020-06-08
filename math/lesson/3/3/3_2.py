# 3. Задание (в программе)
# Напишите код, который будет рисовать график окружности в полярных координатах.

import numpy as np
import matplotlib.pyplot as plot

plot.axes(projection='polar')
rads = np.arange(0, (2*np.pi), 0.01)

for radian in rads:
    plot.polar(radian, 1, '.')

plot.show()


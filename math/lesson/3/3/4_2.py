# 4. Задание (в программе)
# Решите систему уравнений и неравенств:
# y = x2 – 1
# exp(x) + x∙(1 – y) > 1

import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plot


def equation(p):
    x, y = p
    return (y - x**2 + 1, np.exp(x)+x-x*y-1)


x0, y0 = fsolve(equation, (-2, 2))
print(x0, y0)
print(np.exp(x0) + x0*(1-y0), "> 1")


x = np.linspace(-2, 3, 201)
plot.plot(x, x**2-1)
plot.plot(x, (np.exp(x)+x-1)/x)
plot.xlabel("x")
plot.ylabel("y")
plot.grid(True)
plot.show()


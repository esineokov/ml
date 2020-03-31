import matplotlib.pyplot as plot
import numpy as np

x = np.arange(0, 10, 0.1)
y = np.cos(1*x)
z = np.cos(3*x)

plot.plot(x,y)
plot.plot(x,z)
plot.show()


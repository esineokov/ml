# 3. Задание (в программе)
# Напишите код на Python, реализующий построение графиков:
# окружности,
# эллипса,
# гиперболы.

import matplotlib.pyplot as plot
import numpy as np
from matplotlib.patches import Ellipse

# Circle
circle = plot.Circle((0, 0), 5, color='blue', fill=False)
ax = plot.gca()
ax.add_patch(circle)
plot.axis('scaled')
plot.show()

# Ellipse
ellipse = Ellipse(xy=(5, 5), width=2, height=5, angle=np.random.rand()*360)
fig, ax = plot.subplots(subplot_kw={'aspect': 'equal'})
ax.add_artist(ellipse)
ellipse.set_clip_box(ax.bbox)
ellipse.set_alpha(np.random.rand())
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
plot.show()

# Hyperbola
x_min = -20
x_max = 20
dx = 0.1
x_list = np.around(np.arange(x_min, x_max, dx), decimals=4)
y_list = 1 / x_list
plot.plot(x_list, y_list)
plot.show()


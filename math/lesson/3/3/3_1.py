# 3. Задание (в программе)
# Напишите код, который будет переводить полярные координаты в декартовы.
import math


def polar2cart(r, angle):
    x = r*math.cos(angle)
    y = r*math.sin(angle)
    return x, y
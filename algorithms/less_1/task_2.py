# 2. По введенным пользователем координатам двух точек
# вывести уравнение прямой вида y = kx + b, проходящей через эти точки.

# https://drive.google.com/file/d/1f75hFgqV6MoEhTm_QfNzF9xcUslb8TiT/view?usp=sharing

AX = float(input("Введите `x` первой точки: "))
AY = float(input("Введите `y` первой точки: "))

BX = float(input("Введите `x` второй точки: "))
BY = float(input("Введите `y` второй точки: "))

print("Уравнение прямой, проходящей через эти точки:\n")
k = (AY - BY) / (AX - BX)
b = BY - k * BX
print(f"y = {k}*x + {b}")
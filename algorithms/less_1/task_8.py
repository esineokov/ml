# 8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

# https://drive.google.com/file/d/1jLEB6OIJQ80E6DCOVJWqAW5B3gQ3n26T/view?usp=sharing

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
if b > a:
    max_, min_ = b, a
else:
    max_, min_ = a, b

c = int(input("Введите третье число: "))
if c < min_:
    middle = min_
elif c > max_:
    middle = max_
else:
    middle = c

print(f"Среднее число: {middle}")
# 3. Написать программу, которая генерирует в указанных пользователем границах:
# a. случайное целое число,
# b. случайное вещественное число,
# c. случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

# https://drive.google.com/file/d/1Tgal7OKJAD8iQm1xJRVHiK3DNpflTcUG/view?usp=sharing

import random

n1 = int(input("Введите первое челое число: "))
n2 = int(input("Введите второе челое число: "))
print(random.randint(n1, n2))

n1 = float(input("Введите первое вещественное число: "))
n2 = float(input("Введите второго вещественное число: "))
print(round(random.uniform(n1, n2), 2))


n1 = ord(input("Введите первую букву: "))
n2 = ord(input("Введите вторую букву: "))
print(chr(random.randint(n1, n2)))

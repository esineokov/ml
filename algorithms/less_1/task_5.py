# 5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

# https://drive.google.com/file/d/1B-yVSaZo39LpvczEpY5whwGaHoSB1SmK/view?usp=sharing

n = int(input('Введите номер буквы: '))
n = ord('a') + n - 1
print('Это буква:', chr(n))


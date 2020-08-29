# 4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

# https://drive.google.com/file/d/1pVeY2zN00p4XNW3-yEB9FQFFEaA7CEXG/view?usp=sharing

a = ord(input('1-я буква: '))
b = ord(input('2-я буква: '))
a = a - ord('a') + 1
b = b - ord('a') + 1
print('Позиции: %d и %d' % (a, b))
print('Симовлов между буквами', abs(a-b)-1)


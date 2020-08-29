# 7. Определить, является ли год, который ввел пользователь, високосным или не високосным

# https://drive.google.com/file/d/1cQl2-OLlhAJ72z_eB5ubCa2GP9rLAz0i/view?usp=sharing

year = int(input("Введите год: "))
result = False
if year % 4 == 0 or (year % 100 == 0 and year % 400 == 0):
    result = True

print(f"Год {year} {'' if result else 'не '}високосный")
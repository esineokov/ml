def my_func1(x, y):
    return x**y


def my_func2(x, y):
    c = x
    for i in range(1, y):
        x = x * c
    return x


print(my_func1(2, 2))
print(my_func2(2, 2))

print(my_func1(2, 3))
print(my_func2(2, 3))

print(my_func1(12, 2))
print(my_func2(12, 2))

print(my_func1(18, 21))
print(my_func2(18, 21))

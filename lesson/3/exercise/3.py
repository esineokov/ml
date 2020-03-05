def my_func(a, b, c):
    sort = sorted([a, b, c])
    return sort[1] + sort[2]


print(my_func(1, 2, 3))
print(my_func(3, 1, 9))
print(my_func(0, 0, 1))
print(my_func(-5, 5, 0))

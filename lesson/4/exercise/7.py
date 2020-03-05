from functools import reduce


def fibo_gen():
    cur = 1
    stop = 15
    while cur <= stop:
        yield reduce(lambda x, y: x*y, [i for i in range(1, cur+1)])
        cur += 1


for el in fibo_gen():
    print(el)


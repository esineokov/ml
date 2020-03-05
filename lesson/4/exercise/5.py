from functools import reduce

my_list = [i for i in range(100, 1001) if i % 2 == 0] # but better list(range(100, 1000, 2))
print(reduce(lambda x, y: x*y, my_list))


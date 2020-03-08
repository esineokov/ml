from itertools import count, cycle

iterator_a = count(100)
print(next(iterator_a))
print(next(iterator_a))
print(next(iterator_a))

#######################
iterator_b = cycle(["a", "b", "c"])
print(next(iterator_b))
print(next(iterator_b))
print(next(iterator_b))
print(next(iterator_b))


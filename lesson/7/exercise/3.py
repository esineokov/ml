class Cell:
    def __init__(self, count):
        if type(count) != int:
            raise ValueError("Only integer")
        self.count = count

    def __add__(self, other):
        return Cell(self.count + other.count)

    def __sub__(self, other):
        if self.count <= other.count:
            raise ArithmeticError("subtraction of these cells is not possible due to size")
        return Cell(self.count - other.count)

    def __mul__(self, other):
        return Cell(self.count*other.count)

    def __truediv__(self, other):
        result = int(self.count/other.count)
        if result == 0:
            raise ArithmeticError("failed cell division")
        return Cell(int(self.count/other.count))

    def make_order(self, n):
        s = ""
        for i in range(1, self.count+1):
            s += "*"
            if i % n == 0:
                s += "\n"
        return s

    def __str__(self):
        return f"{self.__class__.__name__}: \n{self.make_order(5)}\n"


c1 = Cell(20)
c2 = Cell(5)

print(c1)
print(c1+c2)
print(c1-c2)
print(c1*c2)
print(c1/c2)
print(c1.make_order(10))
print(c1.make_order(4))
print(c2.make_order(2))
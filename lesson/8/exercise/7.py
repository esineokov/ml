class ComplexNumber:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def __str__(self):
        return f"({self.i}{'+' if self.j > 0  else ''}{self.j}j)"

    def __add__(self, other):
        return ComplexNumber(self.i+other.i, self.j+other.j)

    def __mul__(self, other):
        return ComplexNumber((self.i * other.i)+((self.j * other.j)*-1), ((self.i * other.j)+(self.j * other.i)))


a = ComplexNumber(5, -6)
b = ComplexNumber(-3, 2)

a_real = 5-6j
b_real = -3+2j

print("a: ", a, "==", a_real)
print("b:", b, "==", b_real)
print("a+b:", a+b, "==", a_real+b_real)
print("a*b:", a*b, "==", a_real*b_real)


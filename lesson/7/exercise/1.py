class Matrix:
    def __init__(self, data):
        if type(data) != list:
            raise ValueError("data should be list of lists")

        for row in data:
            if type(row) != list:
                raise ValueError("data should be list of lists")

            if len(row) != len(data[0]):
                raise ValueError("all rows in matrix must be the same size")

            for i in row:
                if type(i) not in (int, float):
                    raise ValueError("all elements of matrix must be integer or float type")

        self.data = data
        self._size_h = len(data[0])
        self._size_v = len(data)

    def __str__(self):
        view = ""
        for line in self.data:
            view += f"{line}\n"
        return view

    def __add__(self, other):
        if self._size_h != other._size_h or self._size_v != other._size_v:
            raise ArithmeticError("It is impossible to stack matrices of different sizes.")

        return Matrix([[x + y for x, y in zip(row[0], row[1])] for row in zip(self.data, other.data)])


m1 = Matrix([[1, 2, 3], [2, 3, 4], [3, 4, 5]])
m2 = Matrix([[3, 3, 3], [7, 7, 7], [1, 1, 1]])
print(m1)
print(m2)
print(m1+m2)

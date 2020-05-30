class Data:

    data = None

    def __init__(self, data):
        Data.data = data

    @classmethod
    def parse(cls):
        return list(map(int, cls.data.split("-")))

    @staticmethod
    def validation():
        day, month, year = tuple(Data.parse())
        return 1 <= day <= 31 and 1 <= month <= 12 and year > 0


d = Data("15-10-1987")
print(d.parse())
print(d.validation())

d = Data("44-13-1987")
print(d.parse())
print(d.validation())


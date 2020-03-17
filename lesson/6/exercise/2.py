class Road:
    def __init__(self, length, width):
        if type(length) != int or type(width) != int:
            raise Exception("incoming values should be integer")
        self._length = length
        self._width = width

    def calc(self):
        return self._length*self._width*25*5*0.001


road = Road(20, 5000)
print(road.calc(), " т")


import collections
from itertools import cycle
from time import sleep


class TrafficLight:
    __colors = (
        ("\u001b[41m \u001b[30;1m stop! \u001b[0m", 7),
        ("\u001b[43m \u001b[30;1m ready? \u001b[0m", 2),
        ("\u001b[42m \u001b[30;1m go go go! \u001b[0m", 7),
        ("\u001b[43m \u001b[30;1m ready? \u001b[0m", 2)
    )

    __rules = (
        (__colors[0], __colors[1]),
        (__colors[1], __colors[2]),
        (__colors[2], __colors[1]),
        (__colors[1], __colors[0])
    )

    def __init__(self):
        self.__color = None
        self.__history = collections.deque([], 2)

    def __set_color(self, value):
        if self.__color and ((self.__color, value) not in self.__rules or (self.__color, value) in self.__history):
            raise Exception("Sequence violation!")
        self.__history.append((self.__color, value))
        self.__color = value
        print(value[0])
        sleep(value[1])

    def running(self):
        for i in cycle(self.__colors):
            self.__set_color(i)


# Good script
tl = TrafficLight()
tl.running()

# Bad script
tl = TrafficLight()
tl._TrafficLight__set_color(tl._TrafficLight__colors[0])
tl._TrafficLight__set_color(tl._TrafficLight__colors[2])
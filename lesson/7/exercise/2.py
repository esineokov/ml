from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, title):
        self.title = title

    @abstractmethod
    def _calc_consumption(self):
        pass

    @property
    def consumption(self):
        return self._calc_consumption()


class Coat(Clothes):
    def __init__(self, v, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if type(v) not in (int, float):
            raise ValueError("size must be integer or float type")
        self.v = v

    def _calc_consumption(self):
        return self.v/6.5 + 0.5


class Suit(Clothes):
    def __init__(self, h, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if type(h) not in (int, float):
            raise ValueError("size must be integer or float type")
        self.v = h

    def _calc_consumption(self):
        return 2*self.v + 0.3


coat = Coat(title="autumn coat", v=13)
# print(coat.consumption)

suit = Suit(title="evening suit", h=10)
# print(suit.consumption)

print(f"Total fabric consumption per month:: {(coat.consumption*25)+(suit.consumption*30)}")
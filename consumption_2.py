from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def consumpt(self):
        pass

    def __add__(self, other):
        return self.consumpt + other.consumpt


class Coat(Clothes):
    @property
    def consumpt(self):
        print(f"Consumption of fabric for sewing a coat - {round(self.param / 6.5) + 0.5}")
        return round(self.param / 6.5) + 0.5


class Costume(Clothes):
    @property
    def consumpt(self):
        print(f"Consumption of fabric for sewing a coat - ) - {(2 * self.param +0.3) / 100}")
        return(2 * self.param + 0.3) / 100


coat = Coat(56)
costume = Costume(175)
print(coat + costume)

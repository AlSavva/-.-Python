# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь
# определенное название. К типам одежды в этом проекте относятся пальто и
# костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост
# (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих
# методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на
# этом уроке знания: реализовать абстрактные классы для основных классов
# проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod


class Clothes(ABC):
    name = 'Any'

    @abstractmethod
    def vol_cloth(self):
        return '???'


class Coat(Clothes):

    def __init__(self, size: int):
        self.size = size

    @property
    def vol_cloth(self):
        return round(self.size / 6.5 + 0.5, 3)


class Suit(Clothes):

    def __init__(self, height: float):
        self.height = height

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height < 1.1:
            self._height = 1.1
        elif height > 2.1:
            self._height = 2.1
        else:
            self._height = height

    def vol_cloth(self):
        return self.height * 2 + 3


m = Coat(54)
n = Suit(4)
print(m.vol_cloth)
print(n.vol_cloth())
print(m.vol_cloth + n.vol_cloth())
print(m.size, n.height, Clothes.name, Clothes.vol_cloth(n))

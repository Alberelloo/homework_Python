# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда,
# которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
# параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно. Для определения расхода
# ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов
# на реальных данных. Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod

class Clothes(ABC):

    @abstractmethod
    def expense(self):
        pass

    def total_exprense(self, coats, suits):
        total = 0
        for i in suits:
            total += i.expense
        for i in coats:
            total += i.expense
        return total

class Coat(Clothes):
    def __init__(self, V):
        self.V = V

    @property
    def expense(self):
        return self.V /6.5 + 0.5

class Suit(Clothes):
    def __init__(self, H):
        self.H = H

    @property
    def expense(self):
        return 2 * self.H + 0.3

coat_1 = Coat(40)
coat_2 = Coat(50)
coats =[coat_1, coat_2]

suit_1 = Suit(1.56)
suit_2 = Suit(1.78)
suit_3 = Suit(2)
suits =[suit_1, suit_2, suit_3]

print(coat_2.expense)
print(suit_3.expense)
print(Clothes.total_exprense('self', coats, suits))
# Donder metod metods - magic  metods - double underscore
from Lessons.L3 import Car

class Money:
    def __init__(self,amount=0):
        self.amount = amount

    def __str__(self):
        return f"эксземпляр Money: {self.amount}"

    def __add__(self, other):
        return Money(self.amount)

    def __sub__(self, other):
        return Money (self.amount - other.amount)

    def __mul__(self, other):
        pass

    def __eq__(self, other):
        return self.amount == other.amount

    # gt - greater then - self > other
    # ge - greater then or equal: self >= other
    # lt -
    #

igor_money = Money(100)
print(igor_money)
adilet_money = Money(250)
total_money = igor_money + adilet_money
print(total_money)
print(total_money >  igor_money)

my_car = Car
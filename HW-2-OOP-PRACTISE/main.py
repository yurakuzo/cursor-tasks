class Person:
    def __init__(self, name='anonymous', age=None, money=0, houses=[]):
        self.name = name
        self.age = age
        self.money = money
        self.houses = houses

    def __str__(self) -> str:
        return self.info()
    
    def info(self):
        print(f"{self.name} is {self.age}y.o.\nearns: ${self.money}\nowns: {self.houses}")

    def make_money(self, amount):
        self.money += amount
        self.info()

    def buy_house(self, house):
        self.houses.append(house)
        self.info()
        

class House:
    def __init__(self, area=0, cost=0):
        self.area = area
        self.cost = cost

    def __str__(self) -> str:
        return f"{self.area}m2 house for ${self.cost}"

    def apply_discount(self, discount=.1):
        self.cost *= 1 - discount


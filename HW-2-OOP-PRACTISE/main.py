class Person:
    def __init__(self, name='anonymous', age=None, money=0, houses=[]):
        self.name = name
        self.age = age
        self.money = money
        self.houses = houses
    
    def info(self):
        print(f"{self.name} is {self.age}y.o.\nearns: ${self.money}\nowns: {x if (x := self.houses) else 'no property'}")

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

    def __repr__(self) -> str:
        return f"{self.area}m2 house for ${self.cost}"

    def apply_discount(self, discount=.1):
        self.cost *= 1 - discount

small_typical_house = House(40, 40_000)
villa = House(350, 450_000)
penthouse = House(150, 150_000)

default_person = Person('Jake', 27, 100_000, [small_typical_house])
default_person.info()

rich_person = Person('John', 45, 35_000_000, [villa, penthouse])
rich_person.info()

poor_person = Person('Mike', 17, 50)
poor_person.info()



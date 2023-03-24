# task 1

class Animal:
    def __init__(self, name):
        self.name = name
    
    def __str__(self) -> str:
        return f"{self.__class__.__name__}[{self.name}]"

    def eat(self):
        print(f"{self.name}: eating...")
    
    def sleep(self):
        print(f"{self.name}: sleaping...")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def break_something(self):
        print(f"{self.name}: broke something again...")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def ask_to_go_outside(self):
        print(f"{self.name}: asking to go for a walk...")


class Parrot(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print(f"{self.name}: repeating last TV news...")

    def sing(self):
        print(f"{self.name}: trying to sing...")


class Dolphin(Animal):
    def __init__(self, name):
        super().__init__(name)

    def swim(self):
        print(f"{self.name}: swimming...")


class Elephant(Animal):
    def __init__(self, name):
        super().__init__(name)

    def trumpet(self):
        print(f"{self.name}: trumpets...")


# task 1.a

class Human:
    def __init__(self, name):
        self.name = name
    
    def __str__(self) -> str:
        return f"{self.__class__.__name__}[{self.name}]"

    def eat(self):
        print(f"{self.name}: eating...")
    
    def sleep(self):
        print(f"{self.name}: sleaping...")

    def study(self):
        print(f"{self.name}: studying...")

    def work(self):
        print(f"{self.name}: working...")


class Centaur(Human, Animal):
    def __init__(self, name):
        super().__init__(name)

    def stump_with_hooves(self):
        print(f"{self.name}: stumping with his hooves")
    


# task 2

class Profile:
    def __init__(self,
                 name,
                 last_name,
                 phone_number,
                 address,
                 email,
                 birthday,
                 age,
                 sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex

    # or
    # def __init__(self, **kwargs):
    #     self.__dict__.update(**kwargs)

    def __str__(self) -> str:
        return list(self.__dict__.values())
    

a = Profile('Yura',
            'Kuzo',
            '0632162703',
            'Lviv',
            'yurakuzo20@gmail.com',
            '05.05.2003',
            '19',
            'male')

print(a)


# task 3*

from abc import ABC, abstractmethod

class Laptop(ABC):
    @abstractmethod
    def screen(self):
        pass
    
    @abstractmethod
    def keyboard(self):
        pass
    
    @abstractmethod
    def touchpad(self):
        pass
    
    @abstractmethod
    def webcam(self):
        pass
    
    @abstractmethod
    def ports(self):
        pass
    
    @abstractmethod
    def dynamics(self):
        pass


class HPLaptop(Laptop):
    def screen(self):
        print("HP Laptop Screen")
    
    def keyboard(self):
        print("HP Laptop Keyboard")
    
    def touchpad(self):
        print("HP Laptop Touchpad")
    
    def webcam(self):
        print("HP Laptop Webcam")
    
    def ports(self):
        print("HP Laptop Ports")
    
    def dynamics(self):
        print("HP Laptop Dynamics")


my_laptop = HPLaptop()
my_laptop.screen()  
my_laptop.keyboard()
my_laptop.touchpad()
my_laptop.webcam()  
my_laptop.ports()   
my_laptop.dynamics()

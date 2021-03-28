"""
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def get_name(self):
        return self.name

    def set_name(self):
        return self.sound

dog = Animal("Tommy", "Bark")
print(dog.sound)
cat = Animal("Kitty", "Meaw")
print(cat.name)
"""
"""
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def get_name(self):
        pass

    def set_name(self):
        return self.sound

class Dog(Animal):
    def get_name(self):
        return "Hi. I am a dog.."

class Cat(Animal):
    def get_name(self):
        return "hello. I am a cat. Nice to meet you."

d = Dog("Tommy", "Bark")
print(d.get_name())
c = Cat("Kitty", "Meaw")
print(c.get_name())
"""

"""
class Mammals:
    def get_introduction(self):
        pass

    def get_place(self):
        pass

class Humans(Mammals):
    def get_introduction(self):
        return "I am a homosapiens.."

    def get_place(self):
        return "I live on land.."



class Whale(Mammals):

    def get_introduction(self):
        return "I am a whale.."

    def get_place(self):
        return "I live inside water.."


h = Humans()
w = Whale()


print(h.get_introduction())
print(h.get_place())
print(w.get_introduction())
print(w.get_place())


m = Mammals()
m.get_introduction()
m.get_place()
"""

from abc import ABC, abstractmethod
"""
class Mammals(ABC):

    @abstractmethod
    def get_introduction(self):
        pass

    #@abstractmethod
    def get_place(self):
        pass

class Humans(Mammals):
    def get_introduction(self):
        return "I am a homosapiens.."

    def get_place(self):
        return "I live on land.."



class Whale(Mammals):

    def get_introduction(self):
        return "I am a whale.."

    def get_place(self):
        return "I live inside water.."


h = Humans()
print(h.get_introduction())
print(h.get_place())
"""



class Phone(ABC):

    def get_price(self):
        return self.price

    @abstractmethod
    def get_location(self):
        pass

class TCS(Phone):
    def get_location(self):
        return "location with coordinates.."


class Infosys(Phone):
    def get_location(self):
        return "location without coordinates.."
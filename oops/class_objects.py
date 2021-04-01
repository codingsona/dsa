# oops - object oriented Programming
# everything is onject in python
# cake receipe is class - template or blue print
# every cake is an object

"""
class Animal:
    def __init__(self):
        print("I am inside animal class..")

#print(Animal)
# can you see memory address . no. nothing in memory
# object'll store in memory

#calling method
#Animal()
#result = Animal()
#print(result)


a1 = Animal()
a2 = Animal()
# self ll be replaced by a1,a2 .
"""

"""
class Animal:
    def __init__(self, name):
        print("I am inside animal class.")
        print("i am ", name)



a1 = Animal("dog")
a2 = Animal("cat")
"""




"""
class Animal:
    def __init__(self, name):
        self.name = name
        #a1.name = "cat"
        print("i am ", self.name)
        
a1 = Animal("dog")
a1 = Animal("cat")

# attributes(properties) and behaviour
# behaviour is method
# function and method difference

"""
import inheritance

"""
class Animal:
    def __init__(self):
        print("i am inside animal class.")
    def set_name(self,name):
        self.name = name
    def get_name(self):
        print("i am ", self.name)

a1 = Animal()
a1.set_name("Dog")
a1.get_name()
"""











# Inheritance
# Single Inheritance

"""
class Animal:
    def __init__(self):
        print("i am inside animal class.")

class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("I am dog")

#a1 = Animal()
d1 = Dog()
"""

# multi level inheritance

"""
class A:
    def greet(self):
        print("Hello I am in A.")


class B(A):
    def greet(self):
        #print("Hello I am in B.")
        #pass


class C(B):
    def greet(self):
         #print("Hello I am in C.")
         pass


class D(C):
    def greet(self):
        print("Hello I am in D.")
        pass


d = D()
d.greet()

"""


# multiple inheritance


""" 
class A:
    pass
class B:
    pass
class C(A,B):
    pass
"""

"""
class A:
    def greet(self):
        print("Good morning")

class B:
    def farewell(self):
        print("See you again.")

class C(A,B):
    pass

c = C()
c.greet()
c.farewell()
"""

""" 
class A:
    def greet(self):
        print("Good morning")

class B:
    def farewell(self):
        print("See you again.")

class C(A,B):
    def greet(self):
        print("Good evening")

c = C()
c.greet()
c.farewell()
"""


"""
class A:
    def greet(self):
        print("Good morning")

class B:
    def greet(self):
        print("Good evening")

    def farewell(self):
        print("See you again.")

class C(B, A):
    def greet(self):
        print("Welcome")

c = C()
#c.greet()
#c.farewell()
#print(dir(c))
print(C.mro())
"""

"""
# Diamond
class A:
    def greet(self):
        print("Hello A")
class B(A):
    def greet(self):
        print("Hello B")
    def farewell(self):
        print("Bye B")
class C(A):
    def greet(self):
        print("Hello C")

class D(C, B):
    #def greet(self):
     #   print("Hello D")
     pass

d = D()
d.greet()
"""

""" """
class A():
    def __str__(self):
        return "gm"
    def greet(self):
        print("Hello A.")





a = A()
# print(a)
# a.greet()

# __str__(), __repr__()

print(a.__str__())
#print(a.__repr__())




"""
def myIntroduction1():
    print("Hello")
myIntroduction1()

def myIntroduction2(name):
    print("Hello. My name is", name)
myIntroduction2("Sonali")

def myIntroduction3(name, age):
    print("Hello. My name is", name)
    print("i am", age)
myIntroduction3("Sona", 27)
"""

"""
#myIntroduction3("Sona", 27)

def myIntroduction(name = None, age = None):
    print("Hello. My name is", name)
    print(f'i am {age}')
#myIntroduction("Nils", 72)
"""
def myIntroduction4(*args):
    #print(f'My name and age is {args}')
    print(f'Welcome {args}')
#myIntroduction4(50,90,80)


def myIntroduction5(**kwrgs):
    print(f'My details are {kwrgs["name"]}')

myIntroduction5(name = "sona", age = 27, roll = 90, grade = "A")



#Operator overloading
"""
class A:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return  "x : " + str(self.x) + " y : " + str(self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return  A(x,y)

a1 = A(10,30)
a2 = A(40,60)
#print(a1+a2)

a3 = A("hello","Good morning")
a4 = A(" Sonali", " How was your weekend?")
print(a3+a4)
"""



# "+" operator
a = 50
b = 20
c = a + b
#print(c)


a = "Hello"
b =  str(60)
c = a + b
#print(c)


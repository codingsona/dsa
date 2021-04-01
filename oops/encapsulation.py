"""Capdule- keeping variable and methods inside a wrapper."""
# Finanace
# Sales

# Access Modifiers
class A:
    x = 1 # public variable can be accessed from anywhere
    _y = 2 # protected variable can be accessed from inside the class and the subclass
    __z = 3 # private variable can only be accessed from inside the class

    def test1(self):
        print("I am a public method.")

    def _test2(self):
        print("I am a protected method")

    def __test3(self):
        print("I am a private method.")

    def accessPrivateMembers(self):
        print(self.__z)
        self.__test3()

    def _accessingPrivateByProtected(self):
        print(self.__z)
        self.__test3()



a = A()
"""
print(a.x)
print(a._y)
print(a.__z)
"""
# print(a.test1())
# print(a._test2())
# print(a.__test3())

"""
a.test1()
a._test2()
a.__test3()
"""

"""

a.accessPrivateMembers()

a._accessingPrivateByProtected()
"""



class B(A):
    pass

class C:
    pass

b = B()
c = C()


#print(b.x)
#print(b._y)
#print(b.__z)

"""
print(b.x)
print(c._y)
print(c.__z)
"""


#b.test1()
#b._test2()
#b.__test3()

#b.accessPrivateMembers()
#b._accessingPrivateByProtected()


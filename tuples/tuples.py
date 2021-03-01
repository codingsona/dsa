from typing import NamedTuple
"""
# Arrays are mutable - means it can be changed
# For arr = [1, 2, 3], arr[0] = -100, means that the array is mutable.
# We can change its elements, which is useful, but also means that
# people who are using the array at the same time as us have to put
# up with our changes.
arr = [1, 2, 3,(4,5,6)]
arr[0] = -100
print(arr)




# Tuples are immutables, means it can't be modified. Uncomment below
# lines to see the TypeError exception
tup = (1, 2, 3)
tup[0] = -100
print(tup)



# However, there is an exception. Tuples can contain mutable elements,
# like arrays. Example:
tup = ([0,10], [1], [2])
tup[0][1] = "I just got mutated!"
print(tup)



# So whats the solution? We can make their elements tuples as well!
# Uncomment below lines to see the TypeError exception.
tup = ((0,10), (1), (2))
tup[0][1] = "I just got mutated!"
print(tup)

"""
# Now, what is a NamedTuple? It's a class you can extend, and it makes
# a constructor for you. Let's create a simple class, Animal, with an
# age and a name.
class Animal(NamedTuple):
    age: int
    name: str


# OK, great. Now let's test that the constructor works.
a1 = Animal(12, "Mittu")
print(f"The animal {a1.name} is {a1.age} years old")


# Lets try to change Fido's age. Uncomment to see the exception.
#a1.age = 13


"""
# We could have written this class in the standard Python way as well:
class AnimalWithoutNamedTuple:
    def __init__(self, age, name):
        self.age = age
        self.name = name


# Lets create an animal and try to change their age.
a2 = AnimalWithoutNamedTuple(12, "Fido")
a2.age = 13
print(f"Happy {a2.age}th Birthday, {a2.name}")
"""

# NamedTuple includes a useful built-in method, _replace(), which
# lets you copy a NamedTuple (or, more precisely, a class extending
# NamedTuple) but with one field updated.
a3 = a1._replace(age=13)
print(f"Happy {a3.age}th Birthday, {a3.name}")

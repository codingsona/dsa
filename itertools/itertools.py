"""
Itertools help us create and modify iterators. We can use the itertools package to write performant,
easy-to-understand list processing code. For example: We can use mapping, filtering, and advanced
concepts such as repeat, islice, count, cycle, product, permutations, combinations and ways to combine these.

map: allows to apply a function to all elements of an iterator. Example: to all elements of a list.
filter: allows to keep only the elements of a list that make the function return True.
repeat: takes an object and a number as input and produces an iterator containing that object that many times.
count: starts whatever number is given as input and returns an iterator starting with that number.
cycle: starts with whatever is given as input and returns an iterator repeating that input.
product: produces a cartesian product of two iterators.
permutations: create the permutations of the elements of an iterable.
combinations: create the combinations of the elements of an iterable.
"""


from itertools import repeat, islice, count, cycle, product, permutations, combinations

"""
def add_three(num):
    return num+3


# map: allows to apply a function to all elements of an iterator. Example: to all elements of a list.
before = [1, 2, 3, 4]
after = map(add_three, before)
print("before map: %s \n after map: %s" % (before, list(after)))


def is_lowercase(string):
    return string.islower()

# filter: allows to keep only the elements of a list that make the function return True.
before = ["UPPER", "UPPER", "UPPER", "UPPER"]
after = filter(is_lowercase, before)
print("before filter: %s \n after filter: %s" % (before, list(after)))


before = ["ABC"] # "ABC"
after = repeat(before, 3)
print("before repeat: %s \n after repeat: %s" % (before, list(after)))

# repeat: takes an object and a number as input and produces an iterator containing that object that many times.
before = 10
after = repeat(before, 3)
print("before repeat: %s \n after repeat: %s" % (before, list(after)))

# count: starts whatever number is given as input and returns an iterator starting with that number.
print("sample repeat + islice: %s" % (list(islice(repeat(10, 9), 6))))
print("sample count  + islice: %s" % (list(islice(count(11), 10))))
print("sample cycle  + islice: %s" % (list(islice(cycle(["ABCDE"]), 4)))) # try with "ABC" string



#product: produces a cartesian product of two iterators.
colors = ['green', 'yellow']
sizes = ['S', 'M', 'L']
print("sample product: %s" % list(product(colors, sizes)))


tshirts = product(colors, sizes)
for tshirt in tshirts:
    print(tshirt)


print("sample product: %s" % list(product("ABC", "10")))
print("sample product: %s" % list(product(["ABC"], "10")))

"""
print("sample permutations: %s" % list(permutations(['A', 'B', 'C'])))

print("sample permutations: %s" % list(permutations(['A', 'B', 'C'], r=2)))

print("sample permutations: %s" % list(permutations(["ABC"])))

print("sample combinations: %s" % list(combinations("ABCD", r=2)))

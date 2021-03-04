# Iterator
"""
l = [1, 2, 3, 4, 5]


#for number in l:
#	print(number)

my_iterator = iter(l)

#print(my_iterator)

#print(dir(my_iterator))

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))


l = [number for number in range(1, 100) if number % 2 == 0]
print(l)

"""
# Generator

l = [1, 2, 3, 4, 5]

"""
def test():
	for number in l:
		return number

#result = test()
#print(result)
#print(result)
"""
"""
def test():
	for number in l:
		yield number
"""
"""
result = test()
print(result)
print(result)
print(result)
print(result)
print(result)
"""
"""
my_generator = test()

print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))

"""
t = (number for number in range(1, 10))
print(t)


l1 = [1, 2]

l2 = l1*100000
#print(l2)
#print(l2[100])

def test():
	yield l2[100]

result = test()
print(next(result))

file_name = "central-park-raw.csv"


def csv_reader1(file_name):
    file = open(file_name)
    result = file.read().split("\n")
    return result



def csv_reader2(file_name):
    for row in open(file_name, "r"):
        yield row


# print(csv_reader2(file_name))
#print(csv_reader1(file_name))
"""
csv_gen = csv_reader2(file_name)
row_count = 0

for row in csv_gen:
    row_count += 1

#print(f"Row count is {row_count}")
"""
"""
You can also define a generator expression (also called a generator comprehension),
which has a very similar syntax to list comprehensions. 
"""
csv_gen = (row for row in open(file_name))
#print(next(csv_gen))
#print(next(csv_gen))


"""Building Generators With Generator Expressions"""
nums_squared_lc = [num**2 for num in range(5)]
nums_squared_gc = (num**2 for num in range(5))

# print(nums_squared_gc)
# print(nums_squared_lc)

"""Profiling Generator Performance"""
import sys
nums_squared_lc = [i * 2 for i in range(10000)]
#print(sys.getsizeof(nums_squared_lc) ,"bytes")
#print()

nums_squared_gc = (i ** 2 for i in range(10000))
#print(sys.getsizeof(nums_squared_gc), "bytes")

"""
There is one thing to keep in mind, though. If the list is smaller than the running machine’s available memory, 
then list comprehensions can be faster to evaluate than the equivalent generator expression. To explore this,
let’s sum across the results from the two comprehensions above. 
You can generate a readout with cProfile.run():
"""

import cProfile
cProfile.run('sum([i * 2 for i in range(10000)])')
print()
cProfile.run('sum((i * 2 for i in range(10000)))')

# Note:  If speed is an issue and memory isn’t, then a list comprehension is likely a better tool for the job.


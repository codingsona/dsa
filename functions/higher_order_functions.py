
# Example 1

# define a function that adds 2 to any input integer
def add_two(x):
    return x + 2

# test
assert(add_two(10)) == 12


# define a function that adds 3 to any input integer
def add_three(x):
    return x + 3

# test
assert(add_three(10)) == 13


# Problem: if we had to write dozens or hundreds of similar functions,
# it would get tiring pretty fast!
# Solution: We can write a function that will let us mass produce functions which will add different numbers.

def make_adder(n):
    def adder(x):
        return x + n
    return adder


# generate the function add_four
add_four = make_adder(4)
# generate the function add_five
add_five = make_adder(5)

# test
assert(add_four(10)) == 14
assert(add_five(10)) == 15


# we can even call it directly
assert(make_adder(4)(10)) == 14
assert(make_adder(5)(10)) == 15



# Example2

inData = [
    {
        "name": "",
        "age": 35,
        "salary": 100000,
    },
    {
        "name": "Jane Doe",
        "age": 42,
        "salary": 150,
    },
    {
        "name": "John Doe",
        "age": "15",
        "salary": 200000,
    },
]
print(inData)

# * Ignore any person with an empty name.
# * Ignore any person with an age less than 18.
# * Make sure ages are numbers, not strings.
# * Make sure salaries are numbers, not strings.
# * Convert salaries which are less than $500 from hourly rates to yearly.

def has_empty_name(person):
    return person['name'] == ''

def has_age_under_18(person):
    return person['age'] < 18

def convert_age_to_number(person):
    person['age'] = float(person['age'])

def convert_salary_to_number(person):
    person['salary'] = float(person['salary'])

def convert_salary_to_yearly(person):
    if person['salary'] < 500:
        # 2000 work hours in the year, roughly
        person['salary'] = 2000 * person['salary']


def clean_data(data, cleaners, filters):
    # first make sure the data is cleaned
    for item in data:
        for cleaner_func in cleaners:
            cleaner_func(item)
    # then keep only the good data
    out = []
    for item in data:
        for filter_func in filters:
            # don't add this item if the filter returns False
            if filter_func(item):
                break
            out.append(item)
    return out


outData = clean_data(inData,
    cleaners = [convert_age_to_number, convert_salary_to_number, convert_salary_to_yearly],
    filters = [has_empty_name, has_age_under_18])


print(outData)

"""
"""
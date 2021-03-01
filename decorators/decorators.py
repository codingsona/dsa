# Example1
# We will define a decorator, which will take in a function and print "decorator used".

# Step1: Define the decorator
def testPrint(func):
    # The *args, **kwargs means that whatever inputs were provided (arguments or keyword arguments)
    # will be passed to the inner function.
    def modified( *args, **kwargs):
        print("decorator used")
        return func(*args, **kwargs)
    return modified


# Step2: Test the decorator by defining a decorated function
@testPrint
def sumNumbers(a,b,c):
    print(f'the sum is: {a+b+c}')
    return

# Call the decorated function
sumNumbers(1,2,3)

# Example2
# Define a decorator that prints the duration of a function and prints its input and output


# Step1: import the datetime
from datetime import datetime

# Step2: define the decorator
def timing(func):
    def modified(*args, **kwargs):
        startTime = datetime.now()
        output = func(*args, **kwargs)
        print(f'calling function: {func.__name__} with inputs: {args}, {kwargs}, output: {output} and ExecutionTime: {datetime.now()-startTime}')
        return output
    return modified

from time import sleep

# Step3: Test the decorator by  defining a decorated function
@timing
def sumNumbers(a,b,c):
    sleep(1)
    return a+b+c

# Step4: Call the decorated function
sumNumbers(1,2,c=3)


# Example3
# Write a decorator that calls its wrapped function with fixed input as 1,2,3 and adds 1 to the output.

# Step1: Define the decorator
def callWithFixedInputs(func):
    def modified(*args, **kwargs):
        return func(1,2,3) + 1
    return modified

# Step2: Define the decorated function
@callWithFixedInputs
def sumNumbers(a,b,c):
    return a+b+c

# Step3: Call the decorated function
print(sumNumbers(4,5,6))

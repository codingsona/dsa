from datetime import datetime

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

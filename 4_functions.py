#functions

def add(a, b):
    return a + b

print(add(1, 2))

#functions with default parameters
def add(a, b=2):
    return a + b

print(add(1))

#functions with variable number of arguments
def add(*args):
    return sum(args)

print(add(1, 2, 3, 4, 5))

#functions with keyword arguments
def add(**kwargs):
    return sum(kwargs.values())

print(add(a=1, b=2, c=3))

#functions with both variable number of arguments and keyword arguments
def add(*args, **kwargs):
    return sum(args) + sum(kwargs.values())

print(add(1, 2, 3, 4, 5, a=1, b=2, c=3))

#functions with return statement
def add(a, b):
    return a + b
print(add(1, 2))

#functions with return statement and default parameters
def add(a, b=2):
    return a + b
print(add(1))
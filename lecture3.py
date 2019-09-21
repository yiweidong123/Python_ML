# Methods

# Create a simple list
lst = [1,2,3,4,5,]

# append, count, extent, insert, pop, remove, reverse, sort

lst.append("whatever")
lst.append([12])
lst.append((1,2,4,4,5,5))           # this is appending a tuple 
print(lst)

# List reverse
lst.reverse()
print(lst)

# definitions : methods perform specific actions on an object abd can also take arguments

# print(lst.count())
# means how many times an object appears in your list. (only looks at value at the original list, doesn't count append's value)

# Functions

# Definition: a function is a useful device that groups together and set a statements so they can be run more than once.

# def count(arg1):
#     ...

def name_name_of_function(arg1, arg2):
    '''
    this is where the function's document string (docstrings) goes
    this place tells the developer what this function does
    '''
    # do stuff here
    # return desired result

def say_hello():
    print("h e l l o")

say_hello()


def greeting(name):
    print("hello %s" %(name))

greeting("Michael")

def add_number(num1, num2):
    sum = num1 + num2
    return sum

print(add_number(4.84574, 4.66542574))
print(add_number("one", "two"))

def is_prime(num):
    '''
    Naive method of checking for prime numbers
    '''
    for n in range(2, num):
        if num % n == 0:
            print(f"{num} is not a prime!")
            break
    else: # If number never to 0, then prime
            print(f"{num} is prime")

# is_prime()

import math

def is_prime2(num):
    '''
    Better method
    '''
    if num % 2 == 0 and num > 2:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
        return True

is_prime2(16)

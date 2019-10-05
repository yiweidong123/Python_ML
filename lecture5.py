# Containue our function lessons
# level 2 problems.....

def has_33(nums):
    ''' 
    given a list of intergers, return True if the array contains a 3 next to a 3 somewhere (consecutive)
    has_33([1,3,3]) -> True
    has_33([1,3,1,3]) -> False
    has_33([3,1,3]) -> False
    '''
    #loop through our list
    for i in range(0, len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
            # Creating a window with slicing
            if nums[i:i + 2] == [3,3]:
                return True
    return False

print(has_33([1, 3, 3, 3, 4, 5]))


def paper_doll(text):
    '''
    given a string, reeturn a string where for every character in the original there are 3 characters
    paper_doll('hello') -> hhheeellllllooo
    '''
    result = ""
    for char in text:
        result = result + char * 3
    return result

print(paper_doll('hello'))
print(paper_doll('mississippi'))

def blackjack(card1, card2, card3):
    '''
    given 3 integers between 1 and 11, if their sum is less than or equal to 21, return thier sum.
    If their sum exceeds 21 and there is an 11, reduce the total sum by 10.
    Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

    blackjack(5,6,7) -> 18
    blackjack(9,9,9) -> BUST
    blackjack(9,9,11) -> 19
    '''
    if sum((card1, card2, card3)) <= 21:
        return sum((card1, card2, card3))
    elif sum((card1, card2, card3)) <= 31 and 11 in ((card1, card2, card3)):
        return sum((card1, card2, card3)) - 10
    else:
        return "BUST"
print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))

def spy_games(nums):
    '''
    write a list of integers and return true if tit contains 007 IN ORDER
    '''
    #loop through nums
    code = [0, 0, 7, "x"]
    for num in nums:
        if num == code[0]:
            code.pop(0)# remove the first element in the code list
    return len(code) == 1 #alternatively code[0] == "x" this will return true or false


print(spy_games([1,0,2,4,0,7,5]))
print(spy_games([1,0,2,4,0,5,7]))
print(spy_games([1,7,6,0,0,4,3]))


# Lambda expressions, map and filter functions

# Map Function = allows you to map a function to an iterable object. This means you can quickly call the same function for every item in an iterable, such as a list.

def square(num):
    return num ** 2

my_nums = [1, 2, 3, 4, 5]
map(square, my_nums)
print(list(map(square, my_nums))) # or [nums ** 2 for num in my_nums]
print([num ** 2 for num in my_nums])

def splicer(my_string):
    if len(my_string) % 2 == 0:
        return 'even'
    else:
        return my_string[0]

my_names = ['John', 'Cindy', 'Sarah', 'Kelly', 'Mike']

print(list(map(splicer, my_names)))

# Filter Function = returns an interator yielding hose items but iterable for which function(item) is true. Meaning you need to filter by a function that returns either true or false. Then passing that into filter, along with your iterable, you will get back the only results that would return True from the funtion.

def check_even(num):
    return num % 2 == 0

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Hre we are filtering the nums list by the check_even function
print(list(filter(check_even, nums)))
# Filter will only return the statemnets that are true.


# Lambda expressions = allows us to create something anonymous functions. This means we can quickly made ad-hoc functions without needing to properly define functions with def.
# Function objects returned by running lambda expressions work exactly the same as those created and assigned by defs. There is key difference that makes lambda useful in specialized roles:

# lambda's body is a single expression, not a block of statements.

# The lambda's body is similar to what we would put in a def body's return statement. We simply type the result as an expression instead of explicitly returning it. Because it is limited to an expression, a lambda is less general that a def. We can only squeeze design, to limit program nesting. lambda is designed for coding simple functions, and def handles the larger tasks.

def square((num)):
    result == num ** 2 
    return result

square(2)
#simplify

def square(num): 
    return num ** 2

#one liner

def square(num): return num ** 2
square(2)

square = lambda num : num ** 2
square(2)
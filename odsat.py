# Objects and Data Structures Assessment Test

# Test your knowledge.
# Answer the following questions

# Numbers
# Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to
# 100.25.
# Hint: This is just to test your memory of the basic arithmetic commands, work backwards from 100.25
#--------------------------------Code between the lines!--------------------------------
print(10**2 / 10 * 10 + 1 - 0.75)

#--------------------------------------------------------------------------------------

# Answer these 3 questions without typing code. Then type code to check your answer.
# What is the value of the expression 4 * (6 + 5)
# What is the value of the expression 4 * 6 + 5
# What is the value of the expression 4 + 6 * 5
#--------------------------------Code between the lines!--------------------------------
44
29
34
#--------------------------------------------------------------------------------------


# What is the type of the result of the expression 3 + 1.5 + 4?
#--------------------------------Code between the lines!--------------------------------

float
#--------------------------------------------------------------------------------------


# What would you use to find a number’s square root, as well as its square?
# In [ ]: # Square root:
# In [ ]: # Square:
#--------------------------------Code between the lines!--------------------------------
a = 25 
print(a**(0.5))
print(a**2)

#--------------------------------------------------------------------------------------


# Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:
#--------------------------------Code between the lines!--------------------------------
s = 'hello'
print(s[1])
#--------------------------------------------------------------------------------------

# Print out 'e' using indexing
#--------------------------------Code between the lines!--------------------------------
s = "hello"
print(s[-4])
#--------------------------------------------------------------------------------------


# Reverse the string 'hello' using slicing:
#--------------------------------Code between the lines!--------------------------------
s ='hello'
print(s[::-1])
#--------------------------------------------------------------------------------------


# Given the string hello, give two methods of producing the letter 'o' using indexing.
#--------------------------------Code between the lines!--------------------------------
s ='h(ello'
print(s[-1])
#--------------------------------------------------------------------------------------

# Reassign 'hello' in this nested list to say 'goodbye' instead:
#--------------------------------Code between the lines!--------------------------------
list3 = [1,2,[3,4,'hello']]
list3[2][2] = "Goodbye"
print(list3[2][2])
#--------------------------------------------------------------------------------------

# Dictionaries
#{"key": "value"}
# Using keys and indexing, grab the 'hello' from the following dictionaries:
#--------------------------------Code between the lines!--------------------------------
d = {'simple_key':'hello'}

print(d["simple_key"])
#--------------------------------------------------------------------------------------

# Grab 'hello'
#--------------------------------Code between the lines!--------------------------------
d = {'k1':{'k2':'hello'}}

print(d["k1"]["k2"])
#--------------------------------------------------------------------------------------


# Grab 'hello'
#--------------------------------Code between the lines!--------------------------------
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}

print(d["k1"])                      #[{'nest_key': ['this is deep', ['hello']]}]
print(d["k1"][0])                   #{'nest_key': ['this is deep', ['hello']]}
print(d["k1"][0]["nest_key"])       #['this is deep', ['hello']]
print(d["k1"][0]["nest_key"][1])    #['hello']
print(d["k1"][0]["nest_key"][1][0])
#--------------------------------------------------------------------------------------

#Grab hello
#--------------------------------Code between the lines!--------------------------------
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}

print(d["k1"][2]["k2"][1]["tough"][2][0])
#--------------------------------------------------------------------------------------


# Use a set to find the unique values of the list below:
#--------------------------------Code between the lines!--------------------------------
list5 = [1,2,2,33,4,4,11,22,3,3,2]

answer = set(list5)
print(answer)
#--------------------------------------------------------------------------------------


# Final Question: What is the boolean output of the cell block below?
#--------------------------------Code between the lines!--------------------------------
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]
# True or False?
l_one[2][0] >= l_two[2]['k1']
#false
# This is slightly complex Boolean comparsion....we will take this up in class!
#--------------------------------------------------------------------------------------

# Great Job on your first assessment!
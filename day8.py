# Dictionary:
# Collection of key:value pair inside curly brackets
# Each key:value is separated by comma

# Example:
# a = {}
# a = {
#     'key':'value',
#     (1,2,3):'value2',
#     'key2':[1,2,3,4],
#     'key3':{
#         'a':'b'
#     }
# }
# print(a)
# print(type(a))


# Features:
# 1. ordered
# 2. doesn't allow duplicate
# 3. Doesn't allow indexing
# 4. mutable


# 1. ordered
# a = {
#     'name':'suman',
#     'number':123,
#     'key':'value',
#     'address':'ktm',
#     'gpa':1.1
# }
# print(a)



# 2. duplicates

# a = {
#     'name':'suman',
#     'number':123,
#     'key':'value',
#     'address':'ktm',
#     'gpa':1.1,
#     'name':'suman'
# }
# print(a)


# 3. indexing

# a = {
#     'name':'suman',
#     'number':123,
#     'key':'value',
#     'address':'ktm',
#     'gpa':1.1
# }
# print(a)
# print(a[0])


# 4. mutable
# a = {
#     'name':'suman',
#     'number':123,
#     'key':'value',
#     'address':'ktm',
#     'gpa':1.1,
#     'lname':'suman'
# }
# # a = ['suman',123,'value']
# a['name']='hari'
# print(a)


# Dictionary Methods:

a = {
    1:'value1',
    2:'value2',
    3:'value3',
}

# a[1]='value4'
# a[4]='value4'
# print(a)

# 1. update()   -> to add multiple value to the dictionary
# b = {
#     'name':'ram',
#     'age':12
# }
# a.update(b)
# print(a)

# 2. keys() -> returns all the keys of the dictionary
# print(a.keys())


# 3. values()   -> returns all the values of the dictionary
# print(a.values())

# 4. items()    -> returns all the key-value pair
# print(a.items())

# 5. pop()  -> removes items from the dictionary
# print(a)
# a.pop(2)
# print(a)

# 6. popitem()  -> removes last items from the dictionary
# a.popitem()
# print(a)

# 7. clear()    -> returns empty dictionary
# a.clear()
# print(a)


# del a
# print(a)


# print(len(a))

# Loop with dictionary:

# a = {
#     'key1':'value1',
#     'key2':'value2',
#     'key3':'value3',
#     'key4':'value4'
# }

# for i in a:
#     print(a[i])

# a['key1']



# Function:
# function is a block of code that performs certain action when called


# Two types of functions:
# 1. Built-in function
# 2. User defined function

# 1. Built-in Function
# pre-coded function
# already defined in compiler
# example: print(), len(), max(), min(), sum(), dir(), etc.

# 2. User defined function
# created and used by developers themselves

# Syntax:
# def function_name(argument):  -> function definition:
    # code

# function_name(argument)   -> function call

# a.update()
# print()

# Example:
# def add_two_numbers():
#     a = 1
#     b = 2
#     print(a+b)

# add_two_numbers()
# add_two_numbers()
# add_two_numbers()
# add_two_numbers()


# Types of arguments:
# 1. No argument
# 2. Positional Argument
# 3. Deafault Argument
# 4. Keyword Argument
# 5. Arbitrary Argument / Variable Length Argument
# 6. Arbitrary Keyword Argument / Variable Length Keyword Argument
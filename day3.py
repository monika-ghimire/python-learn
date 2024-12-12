
day = 3
# Data Type:
# classification of data

# A. Numeric Data Type
# 1. integer
# 2. float
# 3. complex    (not important)

# 1. integer:
# a = 123455678
# print(type(a))

# 2. float
# a = 0.0000000001
# print(type(a))

# 3. complex
# a = 2+3j
# print(a)
# print(type(a))

# B. Sequence Data Type
# 1. string
# 2. list (python's array)
# 3. tuple
# 4. range

# 1. string
# collection of character, letter, symbolds, numbers, etc inside quotation symbol
# 'string', "string", """string""", '''string'''
# a = """suman
# is
# my
# name"""
# print(a)
# print(type(a))

# 2. list
# collection of data inside big brackets, each data separated by comma
# example:
# a = [1,2,3,3.12,'suman']
# print(a)
# print(type(a))


# 3. tuple
# collection of data inside small brackets, each data separated by comma
# example:
# a = (1,2,3,3.12,'suman')
# print(a)
# print(type(a))

# 4. range
# collection of integer from start to finish
# syntax:
# range(start,stop,step)

# example:
# a = range(1,11,1)
# print(a)
# print(type(a))


# C. Boolean Data Type
# 1. True
# 2. False


# 1. True
# a = True
# print(type(a))


# 2. False
# a = False
# print(a)
# print(type(a))


# D. Set Data Type
# 1. set
# 2. frozenset  (not important)

# 1. Set
# collection of data inside curly brackets, each data separated by comma
# Example:
# a = {1,2,3.2}
# print(a)
# print(type(a))

# 2. frozenset
# set whose value cannot be changed
# example:
# a = {1,2,3.2}
# b = frozenset(a)
# # print(a)
# print(b)
# print(type(b))


# E. Mapping Data Type
# 1. dictionary

# 1. dictionary
# collection of key:value pair enclosed in curly bracket

# syntax:
"""
my_dict = {
    'key' : 'value',
    'key1' : 'value1',
    'key2' : 'value2',
    .
    .
    'keyN' : 'valueN'
}
"""

# Example:
# my_detail = {
#     'name' : 'suman',
#     'age': 22,
#     'hobbies': ['a','b','c'],
# }
# print(my_detail)
# print(type(my_detail))


# F. None Type
# 1. None

# 1. None
# a = None
# print(a)
# print(type(a))


# G. Binary Data Type (not important)
# 1. bytes
# 2. bytearray
# 3. memoryview


# name = 'ram'
# course = 'MERN'
# age = 12
# gpa = 2.1
# print("my name is",name,"I teach",course,"My age is",age,"My gpa is",gpa)

# my name is ____. My course is ____. My hobby is ____.

# name = 'Suman'
# course = 'Python'
# hobby = 'coding'
# gpa = 2.1
# number = 4
# print("My name is",name+".","My course is",course+".","My hobby is",hobby+".")
# print('a'+'b')

# String Formatting:
# technique of loading variables inside string dynamically

# 1. %
# print("My name is %s. My course is %s. My hobby is %s. My gpa is %.1f"%(name,course,hobby,gpa))

# 2. .format()
# print("My name is {}. My course is {}. My hobby is {}. My gpa is {}".format(name,course,hobby,gpa))

# 3. f-string
# print(f"My name is {name}. My course is {course}. My hobby is {hobby}. My gpa is {gpa}. My number is {number+2}.")




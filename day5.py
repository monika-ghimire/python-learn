day = 5

# String:
# Collection of characters, letters, symbols, etc. inside quotation
# "srting", 'string', """string""", '''string'''

# name = 'suman'
# print(type(name))

# Features:
# 1. allow indexing
# 2. allow duplicate
# 3. ordered
# 4. immutable

# 1. indexing
# way of numbering elements in a collection
# name = 'suman is my name'
# print(name[2])
# print(name[4])
# print(name[-3])


# 2. duplicate
# a = 'string string'
# print(a)

# 3. ordered
# data can be access in the same order as they are stored in
# name = 'suman is my name'
# print(name)

# 4. immutable / not changeable
# original value cannot be modified

# name = 'suman'
# name = 'ram'
# name = [1,2,3]
# name[0] = 'r'
# print(name)


# Slicing:
# way of accessing data from a sequence
# syntax:
# string[start:end:step]    # -> default values: step=1, start=start index of string, end=length of string

# Example:
# name = 'hello, my name is suman.'

# print(name[0:5])
# print(name[7:])
# print(name[:5])
# print(name)
# print(name[::3])
# print(name[::-1])

# WAP to check whether user input string is palindrome or not. Use comparison operator and slicing.
# Example: madam, dad, mom


# Escape Sequence:
"""
1. \n -> new line
2. \t -> horizontal tab
3. \v -> vertical tab
4. \b -> backspace
5. \r -> carriage return/replace first letters
6. \\ -> for backslash
"""

# print('My name\nis suman.')
# print('My name is\tsuman.')
# print('My name is \vsuman')
# print("my name is\b\b\b suman.")
# print('Suman is my name.\rRaman')
# print('My name is suman\\raman\\hari')

# print('Nelson Mandela\'s quote,"I have a dream."')


# String Methods:
# Method syntax:
# string.methodName()


# print(dir(str))   # -> shows the list of method that can be used for a data type


name = 'suman suman GAUTAM GAUTAM'
# print(name)

# 1. strip()  -> removes space from start and end of our string
# print(name.strip())

# 2. print(name.rstrip())
# 3. print(name.lstrip())

# 4. upper()
# print(name.upper())

# 5. lower()
# print(name.lower())

# 6. capitalize()
# print(name.capitalize())

# 7. title()
# print(name.title())

# 8. swapcase()
# print(name.swapcase())

# 9. startswith()
# print(name.startswith('su'))

# 10. endswith()
# print(name.endswith('GAUTAM'))

# 11. replace()
# print(name.replace('suman','ram'))

# 12. removeprefix()
# print(name.removeprefix('suman'))


# 13. removesuffix()
# print(name.removesuffix('GAUTAM'))

# name = 'suman is my name'
# 14. index()
# print(name.index('my'))
# print(name.rindex('m'))

# print(name.count('n'))


# split()
# converts string to list

# print(name.split())

# print(dir(str))
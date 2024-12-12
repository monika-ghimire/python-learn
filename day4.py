day = 4

# Type Conversion:
# Method of converting data type from one type to another

# 1. Implicit
# type conversion done by computer itself without our intervention

# a = 12
# b = 1.2
# c = a+b
# print(c)
# print(type(c))

# 2. Explicit
# converting data from one type to another by developer themselves
# done using casting operator

# a = '1234.123'
# b = int(float(a))
# print(b)
# print(type(b))


# Input function:
# it only takes string as input

# name = input("Enter your name: ")
# print(type(name))
# print(f"My name is {name}.")


# number = int(input("Enter your number: "))
# print(f"If we subtract 2 from {number} we get {number-2}")


# Operators:
# used to perform some operations between two or more variables and values

# 1. Arithmetic Operator
# used to perform operations mainly between numeric data
# +, -, /, *, % (modulus operator/remainder), ** (exponent operator/power), // (Floor division operator)

# a = 21%6
# print(a)

# a = 3**2
# print(a)

# a = 5//2
# print(a)

# 2. Assignment Operator:
# used for assigning right value to left variable
# =, +=, -=, *=, /=, //=, %=, **=

# a = 3
# a += 4  # a = a+4
# print(a)


# 3. Comparison Operator
# Used to compare left and right values
# Only gives Boolean output (True or False)
# ==, !=, <, >, <=, >=

# a = 2
# b = 2
# print(a<=b)


# 4. Logical Operator
# used to check logic of our program
# boolean input and boolean output only
# and, or, not

# print(True and False)
# print(False or False)
# print(not False)

# a = 3
# b = 4
# print(a==3 or b!=3)


# 5. Membership Operator
# used to check if a value is a member of collection data
# only gives boolean output
# in, not in

# a = 'suman'
# a = ['a','e','i','o',5]
# print(5 not in a)

# 6. Identity Operator
# used to compare memory location as well as value
# mutable data takes different memory space for similar data unlike immutable data
# is, is not

# a = (1,2,3)
# b = (1,2,3)
# a = [1,2,3]
# b = [1,2,3]

# print(id(a))
# print(id(b))

# print(a is b)
# print(a == b)


# 7. Bitwise Operator
# used to compare binary numbers
# &, |, ~, ^, <<, >>

# a = 12  # 1100 -> 12
# b = 9   # 1001 -> 9
#         # 1000 -> 8
# print(a & b)


# print(2*8/2+2-5)    # 2*4+2-5    -> 8+2-5   -> 10-5 -> 5

# Precedence:
# BODMAS







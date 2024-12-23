# Write a function to check if a string is a palindrome.
# Example: madam

# def check_pali(string):
#     return string==string[::-1]
# print(check_pali('mada'))


# Ternary Operator:

# a = 3

# if a == 2:
#     print("it is 2")
# else:
#     print("it is not 2")

# print("it is 2") if a ==2 else print("it is not 2")


# List Comprehension:

# for i in range(1,11):
#     if i%2==0:
#         print(i)
#     else:
#         print("hi")

# [print(i) if i%2==0 else print('hi') for i in range(1,11)]

def function_name(a,b,c):
    pass

# Lambda Function:
# anynomous function, one-line function

# Syntax:
# var_name = lambda arguments:expression
# lambda function can have multiple arguments but single expression

# Example:

# add = lambda a,b:(a**2)+(2*a*b)+(b**2)
# print(add(2,3))


# Decorators:
# tool used to modify or add functionality to a function without modifying it

# Nested function:
# def outer():
#     def inner():
#         print("inner")
#     inner()
#     print("outer")
# outer()


# Function as a object/variable
# def some(a):
    # print(a.upper())

# some('hello')

# hello = some
# hello('hello')



# Function as a argument

# def small(text):
#     print(text.lower())

# def big(text):
#     print(text.upper())

# def main(func):
#     func('helLO')

# # main(small)
# main(big)


# Decorator:

# def outer(func):
#     def inner():
#         print('inner')
#         func()
#     return inner

# def main():
#     print("main")

# var = outer(main)
# var()



# def outer(func):
#     def inner():
#         print('inner')
#         func()
#     return inner

# @outer
# def main():
#     print("main")

# main()



# Error handling:

# Error:
# issue that prevents program from executing properly

# 1. Syntax error
# error we get if we don't follow programming syntax properly

# 2. Logical error
# error we get if we apply wrong logic in our program

# def add_two_numbers(a,b):
    # return a-b
# print(add_two_numbers(3,2))

# 3. Runtime error
# error we encounter after execution of program
# ZeroDivisionError, IndexError, TypeError, ValueError, etc.


# Error Handling:

# def div(a,b):
#     print(a/b)
#     print("i am below division")

# div(3,0)


# 1. try        -> code that possibly gives error
# 2. except     -> what to execute after error is encountered
# 3. finally    -> what to execute once the code is successfuly run

# Example1:
# try:
#     # print(3/0)
#     print(3+'3')
#     print("I am below error")
# except:
#     print("Cannot divide by zero")

# finally:
#     print('I am finally done')


# Example2:
# try:
#     print(3/0)
#     print(3+'3')
#     print("I am below error")
# except TypeError:
#     print("Cannot perform such type operation")
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# except:
#     print("I encounted an error")
# finally:
#     print('I am finally done')
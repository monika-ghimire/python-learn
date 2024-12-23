# Types of arguments:
# 1. No argument
# 2. Positional Argument
# 3. Default Argument
# 4. Keyword Argument
# 5. Arbitrary Argument / Variable Length Argument
# 6. Arbitrary Keyword Argument / Variable Length Keyword Argument


# 1. No argument

# def add_two_number():
#     print(1+2)
# add_two_number()


# 2. Positional Argument

# def add_two_number(num1,num2):    # formal argument
#     print(num1)
#     print(num2)

# add_two_number(2,4)     # actual argument


# 3. Default Argument

# def add_two_numbers(a=0,b=0):
#     print(a+b)

# add_two_numbers(5,3)

# 4. Variable Length Argument

# def add_two_numbers(a=0,b=0,*c):
#     print(a+b+sum(c))

# add_two_numbers(5,3,4,5,6)


# 5. Keyword Argument

# def print_something(fname,mname,lname):
#     print(fname,mname,lname)

# print_something(mname='prasad',fname='ram',lname='khadka')


# 6. Variable length keyword argument

# def print_something(**name):
#     print(name['fname'],name['mname'],name['lname'])

# print_something(mname='prasad',fname='ram',lname='khadka')


# Return Keyword:
# can only be used within function
# returns value from the function
# return should contain main output of the function
# return should be the last code of a function
# if value is returned from function, it should be stored when calling the function
# return also works like break statement for function

# Example:

# def add_two_numbers(num1,num2):
#     return num1+num2
#     # print("i am below return")
#     # print(num1+num2)

# number1 = int(input("Enter first number: "))
# number2 = int(input("Enter second number: "))
# a = add_two_numbers(number1,number2)
# print(a)


# Scope:
# 1. Global scope
# 2. Local Scope

# 1. Global
# variable, class, functions created in the main body of python code
# can be accessed from anywhere

# a = 12
# def hello():
#     print(a)

# hello()

# 2. Local Scope
# variable, functions, etc created inside the function
# can only be accessed inside the function

# def something():
#     b = 15
#     def some():
#         print("Some")
#     some()
# some()
# print(b)
# something()

# a = 12
# def something():
#     global a
#     a = 13
#     print(a)
# something()
# print(a)


# def something():
#     a = 12
#     def some():
#         nonlocal a
#         a = 13
#         print(a)
#     some()
#     print(a)

# something()


# Recursive function:
# Recursive function is a function that calls itself until base condition is met

# Syntax:
# def function_name():
    # function_name()


# Example:
# def something():
#     print("Something")
#     something()
# something()


# Example 2:
# def something(n):
#     if n == 10:
#         return
#     else:
#         print("something")
#         something(n+1)
# something(5)

# Example 3:
# 4! = 4*3*2*1  = 24
# 3! = 3*2*1
# 2! = 2*1
# 0! = 1
# 1! = 1

# def fact(n):
#     if n==1 or n==0:
#         return 1
#     elif n<0:
#         return "Invalid number"
#     else:
#         return n*fact(n-1)  # 4*3*2*1

# print(fact(10))
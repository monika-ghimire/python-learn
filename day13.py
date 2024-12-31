# Polymorphism:
# poly = many, morphism = taking forms

# polymorphism in OOP means same function takes many forms


# Example1:
# a = 'ram'
# b = 'hari'
# print(len(a))
# print(len(b))


# Example 2:
# def adding(a,b):
#     return a+b

# print(adding(1,2))
# print(adding('1','2'))


# Types of polymorphism:
# 1. duck type
# same program acts differently in different scenario

# Example:

# class A:
#     def course(self):
#         print("Django")
# django = A()

# class B:
#     def course(self):
#         print("Data Science")
# data = B()

# def show(var):
#     var.course()
# show(django)
# show(data)



# 2. method overloading
# one class has multiple methods with same name bnut different parameter

# Example:

# class A:
#     def adding(self):
#         print("There is nothing to add")
    
#     def adding(self,a):
#         print(a)

#     def adding(self,a,b):
#         print(a+b)

# a = A()
# a.adding(1,2)


# Overload handling:

# class A:
#     def adding(self,a=None,b=None):
#         if a==None and b==None:
#             sum = "Nothing to add"
#         elif a!=None and b==None:
#             sum = a
#         elif a!=None and b!=None:
#             sum = a+b
#         print(sum)

# add = A()
# add.adding(1,2)


# 3. Method Overriding:
# child class and parent class have method with same name and same number of parameters

# example:
# class A:
#     def __init__(self):
#         self.name = 'ram'

#     def show(self):
#         print("Parent class")

# class B(A):
#     def __init__(self):
#         super().__init__()

#     def show(self):
#         super().show()
#         print("Child class")

# b = B()
# b.show()
# print(b.name)


# 4. Operator Overloading

# example:
# a = '1'
# b = '2'
# print(a+b)

# print(1+2)
# print(int.__add__(1,2))

# print(str.__add__('1','2'))

# print(dir(str))


# Dunder (double underscore) function or magic method

# class A:
#     def __init__(self,a):
#         self.a = a

#     def __add__(self,other):
#         return self.a+other.a
    
# obj1 = A(4)
# obj2 = A(2)

# print(obj1+obj2)




# Encapsulation:
# wrapping attribute and method inside a single unit/class


# Example:

# class A:
#     def __init__(self):
#         self.name = 'suman'
# a = A()
# print(a.name)


# Access modifiers:
# techniques used to restrict access of attributes and method globally

# 1. private (__)
# 2. protected (_)


# 1. Private (__)
# variable and methods inside the same class can access but others cannots

# Syntax:
# for attribute:    __attributeName
# for method:   __methodName()

# class A:
#     def __init__(self):
#         self.__name = 'suman'

#     def __some_method(self):
#         print("I am some method")

#     def some(self):
#         print(self.__name)
#         self.__some_method()

# a = A()
# # print(a.__name)
# # a.__some_method()
# a.some()


# 2. protected (_)
# child class and methods, attributes within same class can access others cannot

# Syntax:
# _attributeName
# _methodName()


# class A:
#     def __init__(self):
#         self._name = 'suman'

#     def _some_method(self):
#         print("I am some method")

#     def some(self):
#         print(self._name)
#         self._some_method()

# a = A()
# print(a._name)
# a._some_method()
# a.some()

# class C:
#     def something(self):
#         print(self._name)
# c = C()
# c.something()

# class B(A):
#     def show(self):
#         print(self._name)

# b = B()
# b.show()


# Python doesn't have true encapsulation*

# class A:
#     def __init__(self):
#         self.__name = 'suman'

#     def __some_method(self):
#         print("I am some method")

#     def some(self):
#         print(self.__name)
#         self.__some_method()

# a = A()
# print(a.__name)
# a.__some_method()
# a.some()
# print(a.__dict__)
# print(a._A__name)
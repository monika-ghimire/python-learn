# OOP:

# Class
# Attributes and method


# class A:    # Class
#     # name = 'suman'
#     def something(self):    # method
#         return "I am something"


# a = A()     # Object
# print(a.something())
# print(a.name)



# Constructor:
# special method inside a class
# it gets initialised once object of class is made
# constructor is not supposed to be called like other methods
# __init__()

# Example:

# class A:
#     def __init__(self,n,r):     # constructor
#         self.name = n
#         self.roll = r

#     def something(self):
#         print(f"I am something {self.name}")
    

# a = A('suman',12)
# a.something()

# b = A('ram',14)
# b.something()



# Inheritance:
# One class using attributes and methods of another class
# child class inherits from parent class

# 1. Single Inheritance
# 2. Multiple Inheritance
# 3. Multi Level Inheritance
# 4. Hybrid Inheritance


# 1. Single Inheritance

# class A:
#     def feature1(self):
#         print("I am feature 1")

# class B(A):
#     def feature2(self):
#         print("I am feature 2")

# a = A()
# a.feature1()

# b = B()
# b.feature2()
# b.feature1()



# 2. Multiple Inheritance

# class A:
#     def feature1(self):
#         print("I am feature 1")

# class B:
#     def feature2(self):
#         print("I am feature 2")

# class C(A,B):
#     def feature3(self):
#         print("I am feature 3")

# # a = A()
# # a.feature1()
# # b = B()
# # b.feature2()

# c = C()
# c.feature3()
# c.feature1()
# c.feature2()



# 3. Multi Level Inheritance

# class Grandpa:
#     def feature1(self):
#         print("I am grandpa")

# class Father(Grandpa):
#     def feature2(self):
#         print("I am father")

# class Child(Father):
#     def feature3(self):
#         print("I am child")

# g = Grandpa()
# g.feature1()

# f = Father()
# f.feature1()
# f.feature2()

# c = Child()
# c.feature1()
# c.feature2()
# c.feature3()



# 4. Hybrid Inheritance

# class Grandpa:
#     def feature1(self):
#         print("I am grandpa")

# class Father(Grandpa):
#     def feature2(self):
#         print("I am father")

# class Mother:
#     def mother(self):
#         print("I am mother")

# class Child(Father,Mother):
#     def feature3(self):
#         print("I am child")



# OOP program to calculate total price by taking price and quantity as input

# class Shop:
#     def __init__(self,name,price,quantity):
#         assert quantity>=0 and price>=0, "Quantity and Price should he greater than zero."
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def total_price(self):
#         print(f"Product: {self.name}\nTotal price: {self.price*self.quantity}")

# item_name = input("Enter your item: ")
# item_price = int(input("Enter unit price: "))
# item_quantity = int(input("Enter total quantity: "))

# I1 = Shop(item_name,item_price,item_quantity)
# I1.total_price()


# WAP to take input from user about country, name, year of birth and find his/her current age using OOP

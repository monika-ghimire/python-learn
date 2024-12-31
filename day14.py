# Abstraction:
# used to hide data and complexity of code
# we don't need to know how the code works, we just use the functionality

# Example1:

# from day13 import something
# print(something(1,2))


# In OOP we use abstract class and abstract method for abstract

# Abstract class:
# Blueprint of class
# it contains one or more abstract method

# Abstract method:
# unique method that has declaraction but no implementation

# Things to be noted:
# Object of abstract class cannot be created
# we use abc (abstract base class) module to achieve abstraction
# @abstractmethod decorator is used to make abstract method

# Syntax:

# from abc import ABC, abstractmethod

# class Demo(ABC):    # Abstract class
#     def someMethod(self):
#         pass

#     @abstractmethod
#     def func(self):
#         pass



# Example:

from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def speed(self):    # abstract method
        pass

    def something(self):    # concrete method
        pass

# interface class
# class that contains abstract method only


# class Maruti(Car):
#     def speed(self):
#         print("20 km/hr")
#     def color(self):
#         print("color is brown")

# m = Maruti()
# m.color()

# class Honda(Car):
#     def speed(self):
#         print("50 km/hr")

# h = Honda()
# h.speed()



# Quiz Game:

# class Quiz:
#     def __init__(self,question,answer):
#         self.question = question
#         self.answer = answer

# Question = ["1. What is Python? \na.Programming language\nb.Food\nc.Snake",
#             "2. What is full form of OOP? \na.Nothing \nb.Object of Program \nc.Object Oriented Programming"
#             ]

# Answers = ["a",
#            "c"]
# quiz_list = [ 
#         Quiz(Question[0],Answers[0]),
#         Quiz(Question[1],Answers[1])
# ]

# def fun_quiz(quiz):
#     marks = 0
#     for q in quiz:
#         answer = input(f'{q.question} enter your choice: ')
#         if answer == q.answer:
#             marks+=1
#     print(f"You got {marks} out of {len(Question)} ")

# fun_quiz(quiz_list)


# Jupyter notebook
# numpy, pandas
# matplotlib, tensorflow

# enum(), zip(), filter(), map(),
# file handling
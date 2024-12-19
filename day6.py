# Control Statement:
# keywords used to control flow of program

# 1. break
# can only be used within loops
# breaks the loop

# 2. continue
# can only be used within loop
# skips particular cycle of iteration

# 3. pass
# can be used in any statements that has colon above
# filler


# for i in range(1,6):
#     print(i)
#     if i==3:
#         break


# for i in range(1,6):
#     if i==3:
#         continue
#     else:
#         print(i)


# a = 3
# if a == 3:
#     print("hello")
# elif a == 4:
#     pass


# for i in range(1,5):
#     pass


# While loop:
# indefinite loop
# must contain base condition or break statement
# generally used less than for loop


# while True:
#     print("1.Add\n2.Subtract\n3.Exit")
#     choice = int(input("Enter your choice: "))
#     if choice == 1:
#         num1 = int(input("Enter first number: "))
#         num2 = int(input("Enter second number: "))
#         print(num1+num2)
#     elif choice == 2:
#         num1 = int(input("Enter first number: "))
#         num2 = int(input("Enter second number: "))
#         print(num1-num2)
#     elif choice == 3:
#         break
#     else:
#         print("Enter a valid choice")


# List:
# Collection of data inside a big bracket
# Each data is separated by comma

# Features:
# 1. Allow indexing
# 2. Ordered
# 3. Mutable
# 4. Allow duplicate

# Example: 
# a = [4,2,1,'hari',3.2,2,1,'hari']

# indexing
# print(a[4])

# Ordered
# print(a)

# Mutable
# Orignal data can be modified
# a[0] = 'ram'
# print(a)

# Duplicate
# print(a)

# Slicing:
# Syntax:
# data[startIndex:stopIndex:steps]

# a = [1,2,3,4]
# print(a[0:3])
# print(a[::-1])


# Methods:

# print(dir(list))

# a = [5,4,6,2,7,1]
# print(a)

# 1. append()
# used to add single data in the list
# a.append(0)
# a.append([8,9,0])
# print(a)

# 2. extend()
# used to add multiple value to the list
# a.extend([8,9,0])
# print(a)


# 3. insert()
# used to add data in a particular index
# a.insert(2,'ram')
# print(a)

# a = [1,2,3]
# a[2] = 5
# print(a)


# 4. pop()
# removes item from the last index of list, takes index as argument

# a.pop()
# a.pop(2)
# print(a)


# 5. remove()
# removes item from the list, takes data as argument
# a.remove(7)
# print(a)


# 6. clear()
# removes all data from list
# a.clear()
# print(a)

# del a
# print(a)

# 7. copy()
# copies list to another variable
# b = a.copy()
# a[0]= 9
# print(a)
# print(b)

# Research shallow copy and deep copy in python


# 8. count()
# counts the number of time a particular data appeared in list
# a = [5,4,6,2,7,1,7]
# print(a.count(7))

# 9. index()
# finds index of a data

# a = [5,4,6,2,7,1]
# print(a.index(1))


# 10. sort()
# used to sort data in ascending order
# a = [5,4,6,2,7,1]
# a.sort()
# a.sort(reverse=True)
# print(a)


# 11. sorted()
# used to sort data in ascending order but needs to be stored in different variable
# a = [5,4,6,2,7,1]
# b = sorted(a)

# print(a)
# print(b)


a = [1,2,3,4]

print(min(a))
print(max(a))
print(len(a))
print(sum(a))
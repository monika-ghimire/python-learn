# Tuple:
# collection of data enclosed in small brackets (), each value is separated by comma
# Example:

# a = (1,2,3,4,'hari')
# a = ()
# a = (1,)
# print(a)
# print(type(a))


# Features:
# 1. ordered
# 2. allow duplicates
# 3. allow indexing
# 4. immutable

# 1. ordered
# a = (2,3,5,4,1)
# print(a)

# 2. allow duplicate
# a = (2,3,4,1,2,4,1)
# print(a)

# 3. allow indexing
# a = (2,4,1,2,8)
# print(a[0])

# 4. immutable
# a = (2,3,1,4)
# a[0]=9
# print(a)


# print(dir(tuple))


# Methods:
# a = (4,2,1,1,3,4,5,6)
# print(a.count(4))
# print(a.index(5))

# a = (1,2,3,4,5,6,7,8,9)

# print(len(a))
# print(min(a))
# print(max(a))
# print(sum(a))


# Set:
# Collection of data enclosed within curly brackets {}
# each data is separated by comma

# Example:

# a = {1,2,3,4,5}
# a = set()
# a = {1}
# print(a)
# print(type(a))


# Features:
# 1. unordered
# 2. Doesn't allow indexing
# 3. Doesn't allow duplicate
# 4. Mutable

# 1. unordered
# a = {4,3,2,5,1}
# print(a)

# 2. doesn't allow indexing
# a = {4,3,2,5,1}
# print(a[0])

# 3. duplicates
# a = {4,3,2,5,1,1,2,3,4,5}
# print(a)

# 4. Mutable
# a = {1,2,3,4,5}
# a[0]=9
# Note: can be changed using set methods

# a = {1,2,3,4,5,True}
# print(a)



# Set Methods:
# print(dir(set))

# 1. add()  -> adds a single value to the set
# a = {1,2,3,4,5}
# a.add(8)
# print(a)


# 2. clear()    -> clears the set/returns empty set
# a = {1,2,3,4,5}
# a.clear()
# print(a)


# 3. copy()    -> copy set to new variable
# a = {1,2,3,4,5}
# b = a.copy()
# print(b)


# 4. difference()   -> returns values that are in one set but not in other

# a = {1,2,3,4,5}
# b = {1,3,5}
# c = a.difference(b)
# print(c)


# 5. difference_update()  -> returns values that are in one set but not in other and updates the orginal set
# a = {1,2,3,4,5}
# b = {1,3,5}
# a.difference_update(b)
# print(a)


# 6. symmentric_difference()    -> returns values that are in one set but not in other

# a = {1,2,3,4,5}
# b = {1,3,5,6,7}
# c = a.symmetric_difference(b)
# print(c)


# 7. symmentric_difference_update()    -> returns values that are in one set but not in other

# a = {1,2,3,4,5}
# b = {1,3,5,6,7}
# b.symmetric_difference_update(a)
# print(b)





# 8. update()   -> adds multiple value to the set

# a = {1,2,3,4,5}
# a.update({6,7,8,9,0})
# print(a)


# 9. remove()   -> used to remove value from the set
# a = {1,2,3,4,5}
# a.remove(5)
# print(a)


# 10. discard() -> used to remove value from set
# a = {1,2,3,4,5}
# a.discard(6)
# print(a)

# 11. intersection()    -> returns common items from two or more sets

# a = {1,2,3,4,5}
# b = {2,4,6,8}
# print(a.intersection(b))



# 12. intersection_update()

# a = {1,2,3,4,5}
# b = {2,4,6,8}
# a.intersection_update(b)
# print(a)

# 13. union()   -> returns all the items in both set
# a = {1,2,3,4,5}
# b = {2,4,6,8}
# print(a.union(b))


# 14. isdisjoint()  -> True if none of the items in both set are common

# a = {1,2,3,4,5}
# b = {2,4,6,8}
# print(a.isdisjoint(b))


# 15. issubset()    -> True if all elements in b are in a

# a = {1,2,3,4,5}
# b = {2,4}
# print(b.issubset(a))


# 16. issuperset()  -> True if all elements in a are in b

# a = {1,2,3,4,5}
# b = {2,4}
# print(a.issuperset(b))



# 17. pop() -> removes random values from set
# a = {2,3,4,1,5,9,7}
# a.pop()
# print(a)


# a = {1,2,3,4}
# print(len(a))
# print(min(a))
# print(max(a))
# print(sum(a))


# a = {'a','e','i','o','u'}
# print(a)
# for i in a:
#     print(i)


# frozenset:

# set whose value cannot be changed
# basically makes set immutable

# a = frozenset({1,2,3,4})
# a.add(5)
# print(type(a))



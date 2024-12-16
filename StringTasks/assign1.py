name = "Monika Ghimire"

#  1.	Reverse a string.  

print(name[::-1])

# 2.	Check if a string is a palindrome.
a = input("Enter your name to check: ")
print('1',a == a[::-1])

# 3.	Count the occurrences of a character in a string.
print('2',name.count('m'))

# 4.Convert a string "HELLO WORLD" to lowercase. 
print('4',name.lower())

# 5.	Capitalize the first letter of each word in a sentence. 
print('5',name.capitalize())

# 6.Check if a string contains only numbers.
""" if space ot comma its show False"""
id = '12'
print('6',id.isdigit())

# 7.Replace spaces with underscores in a string.
s = "Replace spaces with underscores"
print('7', s.replace(" ", "_"))
 # Output: Replace_spaces_with_underscores

# 8.Check if a string is a valid number.
s = "123.45"
print('8', s.replace(".", "", 1).isdigit())
  # Output: True

# 9.	Count words in a sentence.
sentence = "Count words in a sentence"
print('9',len(sentence.split()))
 # Output: 5

# 10.Count the number of occurrences of a word in a sentence.
sentence = "apple banana apple cherry apple"
word_to_count = "apple"
count = sentence.split().count(word_to_count)
print('10',count)  # Output: 3

# 11. Convert the string str = "apple banana cherry" to a list of fruits.
s = "apple banana cherry"
print('11', s.split())
 # Output: ['apple', 'banana', 'cherry']

# 12. 	Given a list of string names = ['ram','shyam','hari','manoj'] . Convert the list into string separated by comma. Like this:  ram,shyam,hari,manoj
names = ['ram', 'shyam', 'hari', 'manoj']
result = ",".join(names)
print('12',result)  # Output: ram,shyam,hari,manoj

# 13.Replace the substring "World" with "Python" in the string str = "Hello World" to form a new string "Hello Python".
s = "Hello World"
new_s = s.replace("World", "Python")
print('13',new_s)  # Output: Hello Python








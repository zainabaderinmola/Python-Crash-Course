"""
1) Index to rerun 'how old' 
from string 'Hello there, how old are you'
"""

my_string = 'Hello there, how old are you?'
h_index = my_string.find('how')
d_index = my_string.find('d') + 1
print(f"'how old' will be printed with my_string[{h_index}:{d_index}]")

#2 Result of story[2:4] + story[-1]
story = "Python is awesome"
story_line = story[2:4] + story[-1]
print(f"Output of story[2:4] + story[-1] is '{story_line}'.")

#3 Find len(mystring)
mystring = "Python rocks"
length = len(mystring)
print(f"len(mystring) is: {length}")

#4 Can we change "Rose" to "Pose"
"No. Strings are immutable"

#5 What is word[-4:] * 3
word = 'Python is so cool'
new_word = word[-4:] * 3
print(f"The output of word is: {new_word}")

#6 What code that returns 'pepsi' as "PEPSI"
drink = 'pepsi'
new = drink.upper()
print(f"This code: 'code.upper()' returns {drink} as {new}")

#7 code that returns 'macdonald' as MacDonald
name = 'macdonald'
code = name[:3].capitalize() + name[3:].capitalize()
print(f"This program:'name[:3].capitalize() + name[3:].capitalize()' returns {name} as MacDonald")

#8 code that returns 'MUSHRAH' as 'mushrah'
name = 'MUSHRAH'
lower = name.lower()
print(f"This code: 'name.lower()' changes '{name}' to 'mushrah'.")

#9 built-in method to change string to list
mystring = "Hello World"
code = mystring.split()
print(f" 'mystring.split()' will split {mystring} into {code}.")

#10 Remove "Hello" from "Hello World"
my_string = "Hello World"
new_string = my_string.replace("Hello ", "")
print(f"I will remove Hello from {my_string} using 'my_string.replace('Hello ', '')'.")

#11 Index of first string in a character
print(f"The first index of a string is 0")

#12 Count of 'o' in a string
my_string = "Hello, python is sooo cool"
amount = (my_string.count('o'))
print(f"The number of 'o' in {my_string} is: {amount}")

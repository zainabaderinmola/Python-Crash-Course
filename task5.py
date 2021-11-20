#1. Create a list that contains at least one string,
# one integer and one float
mylist = ["zainab","4","3.5", 'dark', True]

#2. how do I index a nested list? 
# For example if I want to grab 2 from [1,1,[1,2]]
nest = [1,1,[1,2]]
print(f"I can grab the value: {nest[2][1]} using 'nest[2][1]'.")

#3. If lst = [0,1,2]. what is the result of lst.pop()
lst = [0,1,2]
print(f"The value of lst.pop() = {lst.pop()}.")

#4. Lists can have multiple objects/data types? Yes or No?
print("Yes, lists can have multiple data types.")

#5. if lst=['a','b','c'] What is the result of lst[1:]?
lst = ['a','b','c']
print(f"The result of lst[1:] is: {lst[1:]}.")

#6. When do we choose a list and when do we use a dictionary?
print("We use a list for listing out objects while we use a \
dictionary to iterate key-value pairs.")

#7. Create a dictionary with three key-value pair
my_dict = {'name': 'Fatimah', 'age': 6, 'complexion':'dark'}
print(f"An example of a dictionary with three key_value pairs \
is {my_dict}")

#8. Create a dictionary where all the keys are strings, 
# and all the values are integers.
new_dict = {'boy': 12, 'girl': 14, 'mom': 40}
print(f'This is an example of a dictionary having all its \
values as integers: {new_dict}')

#9. Dictionaries retain order and are a sequence
print("Yes, dictionaries retain order \
(since the release of Python 3.7 version) \
but are not a sequence.")

#10. Given d = {'k1':[1,2,3]}. What is the output of d['k1'][1]
d = {'k1':[1,2,3]}
print(f"The output of d['k1'][1] is {d['k1'][1]}.")

#11. Dictionaries are immutable? Yes or No?
print("Yes, dictionaries are mutable")

#12. d = {'simple_key': 'hello'}. Grab 'hello'
d = {'simple_key': 'hello'}
print(f"I can grab 'hello' using: 'd['simple_key'].'")

#13. my_dict = {'k1': {'k2': 'Hello'}}. Grab 'Hello'
my_dict = {'k1': {'k2': 'Hello'}}
grab_hello = my_dict['k1']['k2']
print(f"The output of my code 'my_dict['k1']['k2']' is \
'{grab_hello}'.")

#14. my_dict = {'k1':[{'nest_key':['this is deep',['hello']]}]}. Grab 'hello'
my_dict = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(f"I can grab 'hello' using the code: \
'my_dict['k1'][0]['nest_key'][1][0]'.")

#15. my_dict = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}. Grab 'hello'
my_dict = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print("I can grab 'hello' using the code: \
'my_dict['k1'][2]['k2'][1]['tough'][2][0]'.")

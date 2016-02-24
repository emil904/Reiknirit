""" Create a dictionary """
my_dict = {'name': 'Kiddi'}
print(my_dict)

#Dict's don't have indexes
#We can use the name of the key instead
""" Iteration of dictionaries """
print(my_dict['name'])
my_dict = {'name': 'Kiddi', 'job': 'Student'}
print(my_dict['job'])

#make a dictionary in a dictionary
#notice that last and first get reversed
#dictionary keys dont have an order
name_dict = {'names': {'first': 'Kristinn', 'last': 'Godfrey'}}
print(name_dict)

#call a dict inside a dict
print(name_dict['names']['last'])

#Make a dictionary that keep position of monsters
#(2,2) = monster | (1,2) = not a monster
game_dict = {(2,2): True, (1,2): False}
print(game_dict[(1,2)])


""" Challenge """
my_dict = {'i': 1, 'am': 2, 'what': 20, 'that': 3}
key_list = ['i', 'am', 'what']

def members(my_dict, key_list):
  count = 0
  for word in key_list:
    if word in my_dict.keys():
      count += 1
  print(count)
  return count

members(my_dict, key_list)

#Your code is good but missing one fairly important part. What about words that
#aren't in the dictionary yet? They need to get a count of 1.

#Also, members won't get a key_list argument, only the string to count the words in.

""" Deleting keys"""
#Deleting keys is done the same way as deleting list items
my_dict = {'name': 'Kiddi', 'job': 'Student'}
#delete job key
del my_dict['job']

""" Add a new key"""
my_dict['age'] = 20
#outcome of my_dict is now: {'name': 'Kiddi', 'age': 33}

""" Overwrite a key"""
my_dict['age'] = 21
#you can only owerwrite many keys at once with the inbuilt
#update method:
my_dict.update({'job': 'Student', 'age': 21, 'town': 'Reykjavík', 'name': "Kristinn Godfrey"})
#outcome: mydict = {'town': 'Reykjavík', 'name': 'Kristinn Godfrey', 'job': 'Student', 'age': 21}


""" Challenge """

# E.g. word_count("I am that I am") gets back a dictionary like:
# {'i': 2, 'am': 2, 'that': 1}
# Lowercase the string to make it easier.
# Using .split() on the sentence will give you a list of words.
# In a for loop of that list, you'll have a word that you can
# check for inclusion in the dict (with "if word in dict"-style syntax).
# Or add it to the dict with something like word_dict[word] = 1.

def word_count(some_string):
  string_dict = {}
  for word in some_string.split():
    if word in string_dict:
      string_dict[word] += 1
    else:
      string_dict[word] = 1
  return string_dict
      
""" Name a format placeholder """
my_string = "Hi! My name is {name} and I live in {state}."
#we can do this in either order, it does not matter
my_string.format(name='Kiddi', state='Reykjavik')
""" Iterate over dictionaries """
#Make python pull the keys and values from our
#dict and send then to our function
#We use double asterisk to do that.
my_dict = {'name': 'Kiddi', 'state': 'Reykjavik'}
my_string.format(**my_dict)
#output: 'Hi! My name is Kiddi and I live in Reykjavik.'

#Challenge
dicts = [
    {'name': 'Michelangelo',
     'food': 'PIZZA'},
    {'name': 'Garfield',
     'food': 'lasanga'},
    {'name': 'Walter',
     'food': 'pancakes'},
    {'name': 'Galactus',
     'food': 'worlds'}
]

string = "Hi, I'm {name} and I love to eat {food}"

def string_factory(some_dict, some_string):
  string_list = [] 
  for item in dicts:
    string_list.append(some_string.format(**item))
  return string_list

  



""" Dictionary Iteration """
my_dict = {'name': 'Kiddi', 'age': 20, 'city': 'Reykjavik', 'country': 'Iceland', 'job': 'Student'}
print("my_dict:", my_dict)
print("\nPrint the keys in the dictionary:")
for item in my_dict:
	#Print the keys in the dictionary
	print(item)
	#Print whatevers inside that dictionary for that key
print("\nPrint whatevers inside the dictionary for that key:")
for key in my_dict:
	print(my_dict[key])
print("\nPrint values in dict")
#using values is great cause we don't have to use they key over and over again.
for value in my_dict.values():
	print(value)

""" Teacher stats challenge """
def most_classes(teach_dict):
  max_classes = 0   #Hold the name of the teach with most class
  count = []        # max counter for classes
  for teacher in teach_dict:
    if len(dicts[teacher]) > max_count:
      max_count = len(dicts[teacher])
      most_class = teacher
  return most_class


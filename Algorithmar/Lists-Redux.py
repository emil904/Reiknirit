""" combining list """
# collections = iterables
# strings, list = iterators

#list 1,2,3
a_list = [1,2,3]

#+4, 5 bad practice
a_list.append([4,5])
print ("append = {}.".format(a_list))

#list 0-9
our_list = list(range(10))
print("list range = {}.".format(our_list))

#+=10,11,12 bad practice
our_list += [10, 11, 12]
print("+=10,11,12 = {}.".format(our_list))

""" combining list challenge """
list_1 = list(range(3))
list_2 = ["abc", "def", "ghi"]
list_3 = list_1 + list_2
print(list_3)

""" extend and insert """
#extend instead of a plus operator may be better looking and better for data
our_list.extend(range(13,21))
print(our_list)
#insert lets us put new items in our list at whatever index we want
alpha = list('acdf')
alpha.insert(1, 'b')
alpha.insert(4, 'e')
print(alpha)

""" quiz """
#Q.What is the optional first argument to the str.split() method?
#A.The thing to split the string at

#Q. What does the list() function do?
#A. Creates a new list and turns an iterable into a list

#Q. Which data type does the .join() method belongs to?
#A. String

""" Shopping List Take Three """

#

""" remove lists """

#remove 1 and "a"
remove_list = [1, 2, 3, 4, "a"]
remove_list.remove(1)
remove_list.remove("a")
print (remove_list)

#del index[0] which is 2
del remove_list[0]

print(remove_list)

""" remove lists quiz """

#

""" Disemvoweled """

#

""" Pop """
string_list = ["a", "b", "c", "d"]

#pops the last index ("d")
string_list.pop()
print (string_list)

#we can assign pop value to a variable
c_variable = string_list.pop()
print (c_variable)

#we can pop a variable by index
string_list.pop(0)
#we popped index 0 which is ("a")

print(string_list)

""" Manipulating Lists """
# 1
the_list = ["a", 2, 3, 1, False, [1, 2, 3]]

#pop index 3 to index 0
popped_var = the_list.pop(3)
the_list.insert(0, popped_var)

# 2
the_list.remove("a")
del the_list[3:5]

# 3
the_list.extend(range(4,21))

print(the_list)

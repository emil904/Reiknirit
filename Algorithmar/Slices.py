""" Slices """
my_string = "Hello There"
#slice from range 1-5
print(my_string[1:5])
#slice only index 3
print(my_string[2])
#slice list
my_list = list(range(1,6))
#slice list from range 1-3
#works exactly the same
print(my_list[1:3])
#it always gives a new item 
#of the original type

#slices only go up to the start and stop
#index. We want to give it up to 1
#item past the last index.

#print index 2-5
print(my_list[1:6])

#print index 3-end
print(my_list[2:len(my_list)])

#print index beginning-3
print(my_list[:3])

#print index 3-end
print(my_list[2:])

#print all list
print(my_list[:])

""" copying slices """
#make a copy of a list
my_new_list = [4,2,1,3,5]
my_sorted_list = my_new_list[:]

#sort the sorted list
my_sorted_list.sort()
print(my_sorted_list)

""" slicing with a step """
#slicing with a step of 2.
#That means add 2
#every iterator.
my_list = list(range(20))
print(my_list[::2])

#leave off the zero. We go
#from 2-end and iterate
#every 2nd number.
print(my_list[2::2])

#print the string "Oklahoma",
#every second letter.
print("Oklahoma"[::2])

#print the string "Oklahoma",
#backwards.
print("Oklahoma"[::-1])

#print my_list backwards iterating
#every fifth number.
print(my_list[::-5])

#print my_list backwards 8-2
print(my_list[8:2:-1])

#We can use negative indexes. Here
#we print out 18, cause it's
#the second last iterator.
print(my_list[-2])

""" delete slices """
my_list = [1, 2, 'a', 'b', 'c', 'd', 5, 6, 7, 'f', 'g', 'h', 8, 9, 'j']

#delete first 2 indexes
del my_list[:2]
#delete 8-9 specfically (List redux)
my_list.remove(8)
my_list.remove(9)


""" replace slices """
#replace 5,6,7 with e and f
my_list[4:7] = ['e', 'f']

#now we got the list in alphabetical order
print(my_list[:])

""" find index """
my_list.index('j')


""" Name the three parts of the slice index """
#start stop step
def three_parts(i):
    return i[4:8:2]
listi = [1,2,3,4,5,6,7,8,9,10]
print(three_parts(listi))
#outcome = [5,7]

""" Some functions """
def first_and_last_4(i):
  return i[:4] + i[-4::1]

""" First half lowercased, second half lowercased """
#round(): 0.9997 = 1
#int()  : 0.9997 = 0
def sillycase(string):
    first = string[:round(len(string)/2)].lower()
    second = string[round(len(string)/2):].upper()
    return first+second

import timeit
import random

#array numer 1 = 1000 tolur a milli 1 og 10000
array=[]
for i in range (1000):
    array.append(random.randrange(1,10000))

#array numer 2  = 100 tolur a milli 1 og 10000
array2=[]
for i in range (100):
    array2.append(random.randrange(1,10000))

#array numer 3 = 10000 tolur a milli 1 og 10000
array3=[]
for i in range (10000):
    array3.append(random.randrange(1,10000))

def insertionSort(list):
   for index in range(1,len(list)):

     currentvalue = list[index]
     position = index

     while position>0 and list[position-1]>currentvalue:
         list[position]=list[position-1]
         position = position-1

     list[position]=currentvalue


print(timeit.timeit(str(insertionSort(array))))
print(timeit.timeit(str(insertionSort(array2))))
print(timeit.timeit(str(insertionSort(array3))))

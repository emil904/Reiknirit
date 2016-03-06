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

def quickSort(list):
    less = []
    equal = []
    greater = []

    if len(list) > 1:
        pivot = list[0]
        for x in list:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return quickSort(less)+equal+quickSort(greater)
    else: return list

print(timeit.timeit(str(quickSort(array))))
print(timeit.timeit(str(quickSort(array2))))
print(timeit.timeit(str(quickSort(array3))))

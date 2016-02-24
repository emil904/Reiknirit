import timeit

array=[54,26,93,17,77,31,44,55,20]
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

print(quickSort(array))

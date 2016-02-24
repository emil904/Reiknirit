def binarySearch(listi, hlutur):
    firstItem = 0
    lastItem = len(listi)-1
    found = False

    while firstItem<=lastItem and not found:
        midpoint = (firstItem +lastItem)//2
        if listi[midpoint] == hlutur:
            found = True
        else:
            if hlutur < listi[midpoint]:
                lastItem = midpoint-1
            else:
                firstItem = midpoint+1
    return found
testlisti = [54,26,93,17,77,31,44,55,20]
question = input("Hvada tolu viltu?")
print(binarySearch(testlisti, question))
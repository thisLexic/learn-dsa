def findMissing(array):
    hashMap = {}
    for i in array:
        hashMap[i] = True
    for i in range(len(array)+1):
        if not hashMap.get(i):
            return i

print(findMissing([2, 3, 0, 6, 1, 5]))
print(findMissing([8, 2, 3, 9, 4, 7, 5, 0, 6]))

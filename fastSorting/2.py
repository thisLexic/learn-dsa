def findMissing(array):
    # Time complexity of O(nlogn)
    array.sort()
    length = len(array)
    for i in range(length):
        if array[i] != i:
            return i
    return None

print(findMissing([9, 3, 2, 5, 6, 7, 1, 0, 4]))
print(findMissing([8, 3, 2, 5, 6, 7, 1, 0, 4]))
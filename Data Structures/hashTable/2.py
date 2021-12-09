def findDuplicate(array):
    # Time complexity of O(n)
    hashTable = {}
    for e in array:
        if hashTable.get(e):
            return e
        hashTable[e] = True

print(findDuplicate(["a", "b", "c", "d", "c", "e", "f"]))
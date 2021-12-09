def getOccurOnce(string):
    # Time complexity of O(n)
    hashTable = {}
    for s in string:
        if hashTable.get(s):
            hashTable[s] += 1
        else:
            hashTable[s] = 1
    for s in string:
        if hashTable[s] == 1:
            return s

print(getOccurOnce("minimum"))
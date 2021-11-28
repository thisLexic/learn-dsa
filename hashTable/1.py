def getIntersection(arrayA, arrayB):
    # Time complexity of O(n)
    hashTable = {}
    arrayAnswer = []
    for e in arrayA:
        hashTable[e] = True
    for e in arrayB:
        if hashTable.get(e):
            arrayAnswer.append(e)
    return arrayAnswer

arrayA = [1, 2, 3, 4, 5]
arrayB = [0, 2, 4, 6, 8]
print(getIntersection(arrayA, arrayB))
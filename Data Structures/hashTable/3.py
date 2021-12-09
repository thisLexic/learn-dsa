import string as importString

def findMissingLetter(string):
    # Time complexity of O(n)
    hashTable = {}
    for s in string:
        hashTable[s] = True
    for s in list(importString.ascii_lowercase):
        if not hashTable.get(s):
            return s

print(findMissingLetter("the quick brown box jumps over a lazy dog"))
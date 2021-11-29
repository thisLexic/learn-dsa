def getXIndex(string, count=0):
    # Time complexity of O(n)
    char = string[count]
    if char == "x":
        return count
    return getXIndex(string, count+1)

print(getXIndex("abcdefghijklmnopqrstuvwxyz"))
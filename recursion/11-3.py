def getTriNum(n):
    # Time complexity of O(n)
    if not n:
        return 0
    return n + getTriNum(n-1)

print(getTriNum(7))
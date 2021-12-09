def getUniquePathCount(l,w):
    if l == 1 or w == 1:
        return 1
    return getUniquePathCount(l-1,w) + getUniquePathCount(l,w-1)

l=6
w=4
print(getUniquePathCount(l,w))
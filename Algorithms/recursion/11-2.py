def getEven(array):
    # Time complexity of O(n)
    if not len(array):
        return []
    e = array[0]
    if not e%2:
        return [e] + getEven(array[1:])
    return getEven(array[1:])

array=[1,2,3,4,5,6,7,8,9,10]
print(getEven(array))

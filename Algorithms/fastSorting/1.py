from math import prod

def biggestProductThree(array):
    # Time complexity of O(nlogn)
    array.sort()
    return prod(array[-3:])

print(biggestProductThree([4,0,2,5,1,4,9]))
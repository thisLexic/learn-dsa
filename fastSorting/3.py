def findGreatestN2(array):
    # Time complexity of O(n^2)
    # super slow and unreadable 
    length = len(array)
    for i in range(length):
        isGreatest = True
        for j in range(length):
            if array[j] > array[i]:
                isGreatest = False
                break
        if isGreatest:
            return array[i]

def findGreatestNlogN(array):
    # Time complexity of O(nlogn)
    # slow but very readable
    array.sort()
    return array[-1]

def findGreatestN(array):
    # Time complexity of O(n)
    # fast but not that readable
    greatest = array[0]
    for i in range(1,len(array)):
        ai = array[i]
        if ai > greatest:
            greatest = ai
    return greatest

array=[9, 3, 2, 5, 6, 7, 1, 0, 4]
print(findGreatestN2(array))
print(findGreatestNlogN(array))
print(findGreatestN(array))
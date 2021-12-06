def reverseInPlace(array):
    arrayLen = len(array)
    halfPoint = arrayLen/2
    for i in range(arrayLen):
        if i > halfPoint:
            break
        temp = array[i]
        array[i] = array[arrayLen-i-1]
        array[arrayLen-i-1] = temp

array4 = [1,2,3,4]
reverseInPlace(array4)
print(array4)

array5 = [1,2,3,4,5]
reverseInPlace(array5)
print(array5)
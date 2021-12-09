def getBiggestProduct(array):
    biggest = None
    smallest = None
    maxProduct = 0

    for i in array:
        if i > 0:
            if not biggest:
                biggest = i
                continue
            if i*biggest > maxProduct:
                maxProduct = i*biggest
            if i > biggest:
                biggest = i
        elif i < 0:
            if not smallest:
                smallest = i
                continue
            if i*smallest > maxProduct:
                maxProduct = i*smallest
            if i < smallest:
                smallest = i
    return maxProduct

print(getBiggestProduct([5, -10, -6, 9, 4]))
print(getBiggestProduct([5, 10, -6, 9, -4]))

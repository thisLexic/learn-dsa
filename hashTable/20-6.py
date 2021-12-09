def getLongestConsecutive(array):
    isInArray = {}
    isChecked = {}
    longestCount = 0

    for i in array:
        isInArray[i] = True
    
    for i in array:
        if not isChecked.get(i):
            isChecked[i] = True
            curI = i
            curCount = 1
            while True:
                curI += 1
                if isInArray.get(curI):
                    curCount += 1
                else:
                    break
            if curCount > longestCount:
                longestCount = curCount

    return longestCount

print(getLongestConsecutive([10, 5, 12, 3, 55, 30, 4, 11, 2]))
print(getLongestConsecutive([19, 13, 15, 12, 18, 14, 17, 11]))

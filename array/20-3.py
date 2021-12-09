from math import inf

def findHighestProfit(array):
    smallest = array[0]
    maxProfit = 0
    for i in range(1,len(array)):
        v = array[i]
        if v < smallest:
            smallest = v
        else:
            profit = v - smallest
            if profit > maxProfit:
                maxProfit = profit
    return maxProfit

print(findHighestProfit([10, 7, 5, 8, 11, 2, 6]))
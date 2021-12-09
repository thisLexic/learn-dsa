def nSort(array):
    hashMap = {}
    ans = []
    
    for i in array:
        if not hashMap.get(i):
            hashMap[i] = 1
        else:
            hashMap[i] += 1

    for n in [round(x*0.1, 1) for x in range(970, 991)]:
        for _ in range(hashMap.get(n,0)):
            ans.append(n)

    return ans
        

print(nSort([98.6, 98.0, 97.1, 99.0, 98.9, 97.8, 98.5, 98.2, 98.0, 97.1]))

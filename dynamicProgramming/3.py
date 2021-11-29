def getUniquePathCount(l,w,memo={}):
    # Time complexity of O(n)
    if l == 1 or w == 1:
        return 1

    if not memo.get(l, {}).get(w):
        subSol = getUniquePathCount(l-1,w,memo) + getUniquePathCount(l,w-1,memo)
        if memo.get(l):
            memo[l][w] = subSol
        else:
            memo[l] = {w: subSol}
    return memo[l][w]

l=750
w=750
print(getUniquePathCount(l,w))
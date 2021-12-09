def golomb(n, memo={}):
    # Time complexity of O(n)
    if n == 1:
        return 1
    if memo.get(n):
        return memo[n]
    return 1 + golomb(n - golomb(golomb(n - 1,memo),memo),memo)

print(golomb(23))
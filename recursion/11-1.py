def countChars(array):
    # Time complexity of O(n)
    if len(array) == 0:
        return 0
    return len(array[0]) + countChars(array[1:])

array = ["ab", "c", "def", "ghij"]
print(countChars(["ab", "c", "def", "ghij"]))
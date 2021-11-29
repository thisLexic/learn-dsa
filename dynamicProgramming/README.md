2. The following function uses recursion to calculate the Nth number from
a mathematical sequence known as the “Golomb sequence.” It’s terribly
inefficient, though! Use memoization to optimize it. (You don’t have to
actually understand how the Golomb sequence works to do this exercise.)
def golomb(n)
return 1 if n == 1
return 1 + golomb(n - golomb(golomb(n - 1)));
end

3. Here is a solution to the “Unique Paths” problem from an exercise in the
previous chapter. Use memoization to improve its efficiency:
def unique_paths(rows, columns)
return 1 if rows == 1 || columns == 1
retur
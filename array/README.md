3. Create a new function to reverse an array that takes up just O(1) extra space.

# 20


3. You’re working on some more stock-prediction software. The function
you’re writing accepts an array of predicted prices for a particular stock
over the course of time.
For example, this array of seven prices:
[10, 7, 5, 8, 11, 2, 6]
predicts that a given stock will have these prices over the next seven days.
(On Day 1, the stock will close at $10; on Day 2, the stock will close at
$7; and so on.)
Your function should calculate the greatest profit that could be made
from a single “buy” transaction followed by a single “sell” transaction.
In the previous example, the most money could be made if we bought the
stock when it was worth $5 and sold it when it was worth $11. This yields
a profit of $6 per share.
Note that we could make even more money if we buy and sell multiple
times, but for now, this function focuses on the most profit that could be
made from just one purchase followed by one sale.
Now, we could use nested loops to find the profit of every possible buy-
and-sell combination. However, this would be O(N 2 ) and too slow for our
hotshot trading platform. Your job is to optimize the code so that the
function clocks in at just O(N).

4. You’re writing a function that accepts an array of numbers and computes
the highest product of any two numbers in the array. At first glance, this
is easy, as we can just find the two greatest numbers and multiply them.
However, our array can contain negative numbers and look like this:
[5, -10, -6, 9, 4]
In this case, it’s actually the product of the two lowest numbers, -10 and
-6 that yield the highest product of 60.
We could use nested loops to multiply every possible pair of numbers,
but this would take O(N 2 ) time. Your job is to optimize the function so
that it’s a speedy O(N).
1. Write a function that returns the intersection of two arrays. The intersec-
tion is a third array that contains all values contained within the first two
arrays. For example, the intersection of [1, 2, 3, 4, 5] and [0, 2, 4, 6, 8] is [2, 4] .
Your function should have a complexity of O(N). (If your programming
language has a built-in way of doing this, don’t use it. The idea is to build
the algorithm yourself.)

2. Write a function that accepts an array of strings and returns the first
duplicate value it finds. For example, if the array is ["a", "b", "c", "d", "c", "e",
"f"] , the function should return "c" , since it’s duplicated within the array.
(You can assume that there’s one pair of duplicates within the array.)
Make sure the function has an efficiency of O(N).

3. Write a function that accepts a string that contains all the letters of the
alphabet except one and returns the missing letter. For example, the string,
"the quick brown box jumps over a lazy dog" contains all the letters of the alphabet
except the letter, "f" . The function should have a time complexity of O(N).

4. Write a function that returns the first non-duplicated character in a string.
For example, the string, "minimum" has two characters that only exist
once—the "n" and the "u" , so your function should return the "n" , since it
occurs first. The function should have an efficiency of O(N).

# 20

1. You’re working on software that analyzes sports players. Following are
two arrays of players of different sports:
basketball_players = [
{first_name: "Jill", last_name: "Huang", team: "Gators"},
{first_name: "Janko", last_name: "Barton", team: "Sharks"},
{first_name: "Wanda", last_name: "Vakulskas", team: "Sharks"},
{first_name: "Jill", last_name: "Moloney", team: "Gators"},
{first_name: "Luuk", last_name: "Watkins", team: "Gators"}
]
football_players = [
{first_name: "Hanzla", last_name: "Radosti", team: "32ers"},
{first_name: "Tina", last_name: "Watkins", team: "Barleycorns"},
{first_name: "Alex", last_name: "Patel", team: "32ers"},
{first_name: "Jill", last_name: "Huang", team: "Barleycorns"},
{first_name: "Wanda", last_name: "Vakulskas", team: "Barleycorns"}
]
If you look carefully, you’ll see that there are some players who participate
in more than one kind of sport. Jill Huang and Wanda Vakulskas play
both basketball and football.
You are to write a function that accepts two arrays of players and returns
an array of the players who play in both sports. In this case, that would be:
["Jill Huang", "Wanda Vakulskas"]
While there are players who share first names and players who share last
names, we can assume there’s only one person who has a particular full
name (meaning first and last name).
We can use a nested-loops approach, comparing each player from one
array against each player from the other array, but this would have a
runtime of O(N * M). Your job is to optimize the function so that it can
run in just O(N + M).

2. You’re writing a function that accepts an array of distinct integers from
0, 1, 2, 3…up to N. However, the array will be missing one integer, and
your function is to return the missing one.
For example, this array has all the integers from 0 to 6, but is missing
the 4:
[2, 3, 0, 6, 1, 5]
Therefore, the function should return 4 .
The next example has all the integers from 0 to 9, but is missing the 1:
[8, 2, 3, 9, 4, 7, 5, 0, 6]
In this case, the function should return the 1 .
Using a nested-loops approach would take up to O(N 2 ). Your job is to
optimize the code so that it has a runtime of O(N).

6. You’re writing a function that accepts an array of unsorted integers and
returns the length of the longest consecutive sequence among them. The
sequence is formed by integers that increase by 1. For example, in the
array:
[10, 5, 12, 3, 55, 30, 4, 11, 2]
the longest consecutive sequence is 2-3-4-5. These four integers form an
increasing sequence because each integer is one greater than the previous
one. While there’s also a sequence of 10-11-12, it’s only a sequence of
three integers. In this case, the function should return 4 , since that’s the
length of the longest consecutive sequence that can be formed from this
array.
One more example:
[19, 13, 15, 12, 18, 14, 17, 11]
This array’s longest sequence is 11-12-13-14-15, so the function would
return 5 .
If we sorted the array, we can then traverse the array just once to find
the longest consecutive sequence. However, the sorting itself would take
O(N log N). Your job is to optimize the function so that it takes O(N) time.
1. Given an array of positive numbers, write a function that returns the
greatest product of any three numbers. The approach of using three
nested loops would clock in at O(N 3 ), which is very slow. Use sorting to
implement the function in a way that it computes at O(N log N) speed.
(There are even faster implementations, but we’re focusing on using
sorting as a technique to make code faster.)

2. The following function finds the “missing number” from an array of inte-
gers. That is, the array is expected to have all integers from 0 up to the
array’s length, but one is missing. As examples, the array, [5, 2, 4, 1, 0] is
missing the number 3, and the array, [9, 3, 2, 5, 6, 7, 1, 0, 4] is missing the
number 8.
Here’s an implementation that is O(N 2 ) (the includes method alone is already
O(N), since the computer needs to search the entire array to find n ):
function findMissingNumber(array) {
for(let i = 0; i < array.length; i++) {
if(!array.includes(i)) {
return i;
}
}
// If all numbers are present:
return null;
}
Use sorting to write a new implementation of this function that only takes
O(N log N). (There are even faster implementations, but we’re focusing on
using sorting as a technique to make code faster.)

3. Write three different implementations of a function that finds the greatest
number within an array. Write one function that is O(N 2 ), one that is O(N
log N), and one that is O(N).

# 20

5. You’re creating software that analyzes the data of body temperature
readings taken from hundreds of human patients. These readings are
taken from healthy people and range from 97.0 degrees Fahrenheit to
99.0 degrees Fahrenheit. An important point: within this application, the
decimal point never goes beyond the tenths place.
Here’s a sample array of temperature readings:
[98.6, 98.0, 97.1, 99.0, 98.9, 97.8, 98.5, 98.2, 98.0, 97.1]
You are to write a function that sorts these readings from lowest to highest.
If you used a classic sorting algorithm such as Quicksort, this would take
O(N log N). However, in this case, it’s actually possible to write a faster
sorting algorithm.
Yes, that’s right. Even though you’ve learned that the fastest sorts are
O(N log N), this case is different. Why? In this case, there’s a limited
number of possibilities of what the readings will be. In such a case, we
can sort these values in O(N). It may be N multiplied by a constant, but
that’s still considered O(N).
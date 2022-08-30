Use increasing monotonic stack to get the next smallest and the previous smallest elements. We are calculating how many subarrays the current element will be the minimum in. For example:
​
arr = [2, 3, 4, 1]
​
for each element we find the next smallest and the previous smallest elements.
​
Consider the element 3 ->  Next smallest - 1 -> at index 3, Previous smallest = 2 -> at index 0
​
[2 3 4 1]
[2 3 4] 1
[2 3] 4 1
2 [3 4 1]
2 [3 4] 1
2 [3] 4 1
​
Total number of subarray that 3 is a part of is the number of ways we can place the brackets = (prev_smallest - i) * (next_smallest - i) where i is the index of 3
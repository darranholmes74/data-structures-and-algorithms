# Code Challenge 26

## Insertion Sort

### Code

[insertion sort](code_challenges/insertion_sort.py)

### Tests

[tests for insertion sort](tests/code_challenges/test_insertion_sort.py)

How to run tests?

pytest tests/code_challenges/test_insertion_sort.py

### Pseudocode
Insert(int[] sorted, int value)
  initialize i to 0
  WHILE value > sorted[i]
    set i to i + 1
  WHILE i < sorted.length
    set temp to sorted[i]
    set sorted[i] to value
    set value to temp
    set i to i + 1
  append value to sorted

InsertionSort(int[] input)
  LET sorted = New Empty Array
  sorted[0] = input[0]
  FOR i from 1 up to input.length
    Insert(sorted, input[i])
  return sorted

### Trace

#### Pass 0
The value at index zero is passed over because there is no value to the left.

#### Pass 1

![](code_challenges/assets/insertion_sort/insertion_sort-pass1.png)

In the first pass through of the insertion sort, the 4 at index 1 is evaluated to by checking the left value at index
0 and determines if the value of index 1 is less than the value of index 0. The value of index 0 is indeed greater so the
value of index 0 and 1 swap places.

#### Pass 2

![](code_challenges/assets/insertion_sort/insertion_sort-pass2.png)

In the second pass the value of index 1 is evaluated to check if index 1 is less than the value of
index 0. The value evaluate to index 1 being greater than index 0 so index 0 and 1 do not change.


#### Pass 3

![](code_challenges/assets/insertion_sort/insertion_sort-pass3.png)

In the third pass the value of index 2 is evaluated to check if index 2 is less than the value of
index 1. The value evaluate to index 2 being greater than index 1 so index 1 and 2 do not change.

#### Pass 4

![](code_challenges/assets/insertion_sort/insertion_sort-pass4.png)

In the fourth pass the value of index 3 is evaluated to check if index 3 is less than the value of
index 2. The value evaluate to index 3 being greater than index 2 so index 2 and 3 do not change.

#### Pass 5-6

![](code_challenges/assets/insertion_sort/insertion_sort-pass5-6.png)

In the fifth pass through of the insertion sort, the value at index 4 is evaluated to by checking the left value at index
3 and determines if the value of index 4 is less than the value of index 3. The value of index 3 is indeed greater so the
value of index 3 and 4 swap places. The process for pass 4 is repeated on pass 6 for index  and 3.

#### Pass 7-9

![](code_challenges/assets/insertion_sort/insertion_sort-pass7-9.png)

In the seventh pass through of the insertion sort, the value at index 5 is evaluated to by checking the left value at index
4 and determines if the value of index 5 is less than the value of index 4. The value of index 4 is indeed greater so the
value of index 4 and 5 swap places. The process for pass 5 is repeated on pass eight for index 4 and 3 and pass nine for index 3 and 2.


### Efficency

 - Time: O(n^2): each element of the list the algorithm has to iterate over the previously sorted portion of the list to find the correct position.

 - Space O(1): The algorithm will only use a constant amount of extra memory





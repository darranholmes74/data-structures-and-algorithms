# Code Challenge 27

## Merge Sort

### Code

[insertion sort](code_challenges/sorting/merge.py)

### Tests

[tests for insertion sort](tests/code_challenges/test_sorting_merge.py)

How to run tests?

pytest tests/code_challenges/test_sorting_merge.py

### Pseudocode
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left


### Trace

#### Part 1

![](code_challenges/sorting/merge_assets/sorting-merge-part1.png)

The function recursively passes over the array until the length of each array is == 1

#### Part 2

![](code_challenges/sorting/merge_assets/sorting-merge-part2.png)

Each function compares the left array to the right array checking to see if the value is smaller or greater than the other.
If value is smaller, it added the value to a new array.

#### Part 3

![](code_challenges/sorting/merge_assets/sorting-merge-part3.png)

In the third pass the function compares the most left of left array to the most left of the right array adds the smallest value to the new array.
This process continues until the array is completely sorted.


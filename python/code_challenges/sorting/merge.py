def mergesort(arr):
    n = len(arr)
    if n > 1:
        mid = n // 2
        left = arr[:mid]
        right = arr[mid:]
        # sort the left side
        mergesort(left)
        # sort the right side
        mergesort(right)
        # merge the sorted left and right sides together
        merge(left, right, arr)


def merge(left, right, arr):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # copy remaining elements of left or right if any
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


arr = [8, 4, 23, 42, 16, 15]
mergesort(arr)
print(arr)  # [3, 9, 10, 27, 38, 43, 82]


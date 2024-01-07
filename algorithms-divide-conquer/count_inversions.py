import math

from typing import List


def count_inversions(arr: List[int]):
    if len(arr) == 0 or len(arr) == 1:
        return [0, arr]
    len_arr = len(arr)
    left_inv, left_sorted = count_inversions(arr[:len_arr // 2])
    right_inv, right_sorted = count_inversions(arr[len_arr // 2:])
    left_len = len(left_sorted)
    right_len = len(right_sorted)
    i = j = k = 0
    split_inversion = 0
    while i < left_len and j < right_len:
        if left_sorted[i] < right_sorted[j]:
            arr[k] = left_sorted[i]
            split_inversion += j
            i += 1
        else:
            arr[k] = right_sorted[j]
            j += 1
        k += 1
    while i < left_len:
        arr[k] = left_sorted[i]
        split_inversion += j
        i += 1
        k += 1
    while j < right_len:
        arr[k] = right_sorted[j]
        j += 1
        k += 1
    return [left_inv + right_inv + split_inversion, arr]


print(count_inversions([2, 1, 3, 4, 5]))

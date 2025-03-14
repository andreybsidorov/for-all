def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

import random

left = sorted([random.randint(1, 50) for _ in range(5)])
print('Left: ', left)
right = sorted([random.randint(1, 50) for _ in range(5)])
print('Right: ', right)

after_merge = merge(left, right)
print('After merge: ', after_merge)

def merge_sort(array):
    if len(array) <= 1:
        return array
    # Разделяем массив на две половины
    middle = len(array) // 2
    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])
    # Сливаем отсортированные половины
    return merge(left, right)

import random

arr = [random.randint(1, 50) for _ in range(10)]
print('Before merge_sort: ', arr)

sorted_arr = merge_sort(arr)
print('After merge_sort: ', sorted_arr)


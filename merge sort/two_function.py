""" two function approch using recursion """

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    return merge(sorted_left,sorted_right)

def merge(left,right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])

    return result


my_arr = [3, 7, 6, -10, 15, 23.5, 55, -13]
print(my_arr)

sort = merge_sort(my_arr)
print(sort)

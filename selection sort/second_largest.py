# Use sorting (bubble or selection) to find the second largest number.

def second_largest(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]
    largest = arr[-1]
    for k in range(n-2, -1, -1):
        if arr[k] < largest:
            return arr[k]
    # return arr[-2]

my_arr = [12, 35, 1, 10, 35, 1]

a = second_largest(my_arr)
print(f"second largest number in array is :{a}")

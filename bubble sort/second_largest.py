# Use sorting (bubble or selection) to find the second largest number.

def second_largest(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    largest = arr[-1]
    for k in range(n-2,-1,-1):
        if arr[k] < largest:
            return arr[k]

my_arr = [12, 35, 1, 10, 35, 1]

a = second_largest(my_arr)
print(f"second largest number in array is :{a}")

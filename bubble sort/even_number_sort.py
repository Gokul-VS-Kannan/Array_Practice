# Sort only the even numbers, keep odd numbers in their original position.
# Input: [9, 4, 2, 7, 6, 5]

# Output: [9, 2, 4, 7, 6, 5]

def even_number_sort(arr):
    n = len(arr)
    for i in range(n-1):
        if arr[i]%2==0:
            for j in range(i+1,n):
                if arr[j]%2==0 and arr[j] < arr[i]:
                     arr[i], arr[j] = arr[j], arr[i]   
    return arr

my_arr = [8, 5, 4, 7, 6, 4,5]
a= even_number_sort(my_arr)
print(a)

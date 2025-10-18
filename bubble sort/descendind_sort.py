# Modify your code so the output is in descending order.

def descending_sort(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped =True
        if not swapped:
            break
    print(f"sorted array is : {arr}")

my_arr =[55,2,11,5,40,98,20,22,5]
descending_sort(my_arr)
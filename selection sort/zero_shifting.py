# Move all zeros to the end using sorting logic


def zero_shift(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[j]!=0 and arr[min_index]==0:
                arr[j],arr[min_index]=arr[min_index],arr[j]
    return arr

my_arr =[1,2,0,0,5,9,0,4,6,0,7,9]
print(f"original array is : {my_arr}")

a = zero_shift(my_arr)
print(f"new array after shifting zero is : {a}")
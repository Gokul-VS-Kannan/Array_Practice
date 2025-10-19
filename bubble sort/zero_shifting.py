# Move all zeros to the end using sorting logic

def zero_shift(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]==0 and arr[j+1]!=0:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

my_arr =[1,2,0,0,5,9,0,4,6,0,7,9]
print(f"original array is : {my_arr}")

a = zero_shift(my_arr)
print(f"new array after shifting zero is : {a}")
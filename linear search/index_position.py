# Write a program to check if a number exists in the list using linear search.

arr_1 = [10,20,30,70,45,5]

target = 20

def check(arr_1,target):
    n=len(arr_1)
    for i in range(n):
        if arr_1[i] == target:
            print(f"{target} found at index {i}")  
            break    
    else:
        print(f"{target} is not in the given array")  
check(arr_1,target)
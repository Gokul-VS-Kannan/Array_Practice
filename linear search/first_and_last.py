# Find the first and last position of an element.

arr_1 = [3,7,5,5,8,6,5,7]
target = int(input("Enter the number whose value you want to find :"))

def first_last(arr,value):
    first = -1
    last = -1
    n = len(arr)

    for i in range(n):
        if arr[i] == value:
            if first == -1:
                first = i
            last = i

    if first != -1:
        if first == last:
            print(f"{value} occurs only once at index {first}")
        else:
            print(f"{value} first found at index {first}")
            print(f"{value} last found at index {last}")
    else:
        print(f"{value} does not exist in the array")

first_last(arr_1,target)
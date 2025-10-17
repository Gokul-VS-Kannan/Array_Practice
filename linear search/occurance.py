# Find how many times an element occurs in the list.

arr_1 = [3,2,5,3,6,7,3,10,3,5]

target = int(input("Enter the number which you want to fount the count :"))

def count(arr,value):
    occurance = 0
    n = len(arr)

    for i in range(n):
        if arr[i] == value:
            occurance +=1

    print(f"{value} repeats {occurance} times in the array")

count(arr_1,target)
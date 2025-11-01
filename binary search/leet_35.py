"""Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity."""

class solution:
    def search_insert(self,nums:list[int],target:int) ->int:
        l = 0
        r = len(nums)-1
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m+1
            else:
                r = m-1
        return l
    
obj1 = solution()
arr_1 = [1,3,5,6]
t_1 = 5
t_2 = 2
t_3 = 7

print(obj1.search_insert(arr_1,t_1))
print(obj1.search_insert(arr_1,t_2))
print(obj1.search_insert(arr_1,t_3))
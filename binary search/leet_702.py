'''Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.'''

class solution :
    def search(self,nums:list[int], target:int) ->int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid =(left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return -1
    

obj1 = solution()
arr_1 = [-1,0,3,5,9,12]
t_1 = 9

print(obj1.search(arr_1,t_1))
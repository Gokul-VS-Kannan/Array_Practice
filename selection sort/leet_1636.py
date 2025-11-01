""" Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

Return the sorted array.

 

Example 1:

Input: nums = [1,1,2,2,2,3]
Output: [3,1,1,2,2,2]
Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.
Example 2:

Input: nums = [2,3,1,3,2]
Output: [1,3,3,2,2]
Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.
Example 3:

Input: nums = [-1,1,-6,4,5,-6,1,4,1]
Output: [5,-1,4,4,-6,-6,1,1,1] """
 

class Solution:
    def frequencySort(self, nums:list[int]) -> list[int]:
        n = len(nums)

        for i in range(n):
            min = i
            for j in range(i+1,n):

                count_i = 0
                for x in range(n):
                    if nums[x] == nums[min]:
                        count_i += 1
                
                count_j = 0
                for x in range(n):
                    if nums[x] == nums[j]:
                        count_j += 1

                if count_j < count_i:
                    min = j
                elif count_j == count_i and nums[j] > nums[min]:
                    min = j
            
            if min != i:
                nums[i],nums[min] = nums[min],nums[i]
        
        return nums


obj_1 = Solution()

arr_1 = [1,1,2,2,2,3]
arr_2 = [2,3,1,3,2]
arr_3 = [-1,1,-6,4,5,-6,1,4,1]

print(obj_1.frequencySort(arr_1))
print(obj_1.frequencySort(arr_2))
print(obj_1.frequencySort(arr_3))
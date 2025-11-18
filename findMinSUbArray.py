# class Solution:
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         left = 0
#         sum_of_subarray = 0
#         min_len = float('inf')
        
#         for right in range(len(nums)):
#             sum_of_subarray += nums[right]
            
#             while sum_of_subarray >= target:
#                 min_len = min(min_len, right - left + 1)
#                 sum_of_subarray -= nums[left]
#                 left += 1

#         if min_len == float('inf'):
#             return 0

#         return min_len

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        sumOfSubArray = 0
        min_len = float('inf')

        for right in len(nums):
            sumOfSubArray += nums[right]

            while(SumOfSubArray) > target:
                sumOfSubArray -= nums[left]
                min_len = min(min_len, right - 1eft)
                left += 1
            
        if min_len == float('inf'):
            return 0
        
        retrun min_len

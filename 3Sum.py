class Solution:
    def threeSum(self, nums: List[int])->List[List[int]]:
        nums.sort()
        my_List = []
        left = 0
        right = 0

        for i in range(len(nums)):
            if i > 0 and nums[i] ==  nums[i-1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    my_List.append([nums[i], nums[left], nums[right]])
                    left += 1
                    
                    while left < right and nums[left] == nums[left-1]:
                        left +=1

                elif sum < 0:
                    left +=1
                else:
                    right -= 1
                
        return my_List

#     # Solution 2
# class Solution:
#     def threeSum(self, num: List[int]) -> List[int]:
#         res = []
#         num.sort()

#         for i in range(len(num)):
#             if i > 0 and num[i] == num[i - 1]:
#                 continue
                
#             j = i + 1
#             k = len(num) - 1

#             while j < k:

#                 sum = num[i] + num[j] + num[k]

#                 if sum < 0:
#                     j += 1
                    
#                 if sum > 0:
#                     k -= 1

#                 if sum == 0:
#                     res.append([num[i], num[j], num[k]])
#                     j += 1
#                     while num[j] == num[j -1] and j < k:
#                         j += 1
                    

#         return res     

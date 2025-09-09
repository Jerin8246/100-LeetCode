# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         my_dict = defaultdict(int)
#         max = len(nums)/2
         
#         for num in nums:
#             my_dict[num] += 1
        
#         for key in my_dict:
#             if my_dict[key] >= max:
#                 return key

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        my_dict = {}
        max = len(nums)/2

        for i in nums:
            if i not in my_dict:
                my_dict[i] = 1
            else:
                my_dict[i] += 1

        for key in my_dict:
            if my_dict[key] >= max:
                return key

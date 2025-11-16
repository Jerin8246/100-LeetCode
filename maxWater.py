# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         left = 0
#         right = len(height) - 1
#         maxArea = 0
        
#         if len(height) == 0:
#             return 0

#         while left < right:
#             area = (right - left) * min(height[left], height[right])
#             if height[left] > height[right]:
#                 right -= 1
#             else:
#                 left +=1
#             if area > maxArea:
#                 maxArea = area

#         return maxArea

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxWater = 0
     
        left, right = 0, len(height) - 1
        
        if len(height) == 0:
            return 0
        
        while left < right:
            x = right -left
            y = min(height[left], height[right])
            volume = x * y
            maxWater = max(volume, maxWater)
            
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return maxWater


            
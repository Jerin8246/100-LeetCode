class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        temp = []
        for i in nums:
            temp.append(i)
    
        for i in range(len(temp)):
            index = (i + k) % len(temp)
            nums[index] = temp[i]

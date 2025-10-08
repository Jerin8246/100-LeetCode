class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        my_set = set()
        index = 0
        for i in nums:
            my_set.add(i)
        nums.clear()
        for element in my_set:
            nums.append(element)
        nums.sort()
        return len(nums)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gas = nums[0]
        for i in range (1, len(nums)):
            gas -= 1
            if gas < 0:
                return False
            if gas < nums[i]:
                gas = nums[i]

        if gas >= 0:
            return True
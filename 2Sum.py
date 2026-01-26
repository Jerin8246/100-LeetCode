
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = defaultdict(int)

        for i in range(len(nums)):
            map[nums[i]] = i
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in map and map[complement] != i:
                return [i, map[complement]]



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = defaultdict(int)

        for i in range(len(nums)):
            map[nums[i]] = i
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in map and map[complement] != i:
                return [i, map[complement]]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        map = defaultdict(int)

        for i, num in enumerate(nums):
            if target - num in map:
                return [i , map[target - num]]
            map[num] = i
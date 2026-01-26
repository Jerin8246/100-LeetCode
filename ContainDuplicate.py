class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map = defaultdict(int)
        for i, num in enumerate(nums):
            if num in map:
                if abs(map[num] - i) <= k:
                    return True
            map[num] = i
        
        return False
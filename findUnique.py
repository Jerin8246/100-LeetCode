class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        map = defaultdict(int)

        for n in arr:
            map[n] += 1

        v = map.values()
        uv = set(v)

        return len(v) == len(uv)
        

# class Solution:
#     def uniqueOccurrences(self, arr: List[int]) -> bool:
#         map = defaultdict(int)

#         for num in arr:
#             map[num] += 1
        
#         setCounter = set()

#         for num in map.values():
#             if num in setCounter:
#                 return False
#             setCounter.add(num)

        
#         return True
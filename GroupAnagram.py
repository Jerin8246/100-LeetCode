# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         anagram_map = defaultdict(list)

#         #list.sort() only work in list but sorted(list) work in any iterable like list, string, dict       
#         for word in strs:           
#             sorted_word = ''.join(sorted(word))  # sorted(word) will return list so we need to use .join      
#             anagram_map[sorted_word].append(word)
        
#         return list(anagram_map.values())

## Solution 2
    
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            maps[sorted_word].append(word)
        
        return list(maps.values())
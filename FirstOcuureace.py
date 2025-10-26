class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        idx = 0
        l = len(haystack)

        if len(needle) > len(haystack):
            return -1
        if len(needle) == '':
            return 0
        
        letters = [[] for _ in haystack]

        for i in range(len(haystack) - len(needle) + 1):
            letters[idx] = haystack[i:i + len(needle)]
            idx += 1
        
        for i in range(len(letters)):
            if needle in letters[i]:
                    return i
            
        return -1

            
# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         # If needle is empty, by convention return 0
#         if needle == "":
#             return 0

#         # If needle is longer than haystack, it can't exist inside
#         if len(needle) > len(haystack):
#             return -1

#         # Sliding window approach
#         for i in range(len(haystack) - len(needle) + 1):
#             if haystack[i:i+len(needle)] == needle:
#                 return i
        
#         return -1


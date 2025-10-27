#My solution
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:  # Empty string is always a subsequence
            return True

        index1 = 0
        index2 = 0

        for _ in range(len(t)):
            if s[index1] == t[index2] :
                index1 += 1
                index2 += 1
            else:
                index2 += 1
            
            if index1 == len(s):
                return True

        return False

# # Provided Solution
# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         i, j = 0, 0
#         while i < len(s) and j < len(t):
#             if s[i] == t[j]:
#                 i+= 1
#             j+=1
        
#         return i == len(s)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0

        for c in t:
            if s[i] == c:
                i += 1
        
        return i == len(s)

# 345. Reverse Vowels of a String
# 
# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "IceCreAm"

# Output: "AceCreIm"

# Explanation:

# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:

# Input: s = "leetcode"

# Output: "leotcede"

 

# Constraints:

# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.


###################################################################################################################
# class Solution:
#     def reverseVowels(self, s: str) -> str:
#         i = 0
#         j = len(s) - 1
#         s = list(s)
#         vovels = ['a','e','i','o','u', 'A','E','I','O','U']
#         while i < j:
#             if s[i] not in  vovels:
#                 i += 1
#             elif s[j] not in vovels:
#                 j -= 1
#             else:
#                 s[i], s[j] = s[j], s[i]
#                 i += 1
#                 j -= 1
        
#         return ''.join(s)

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=[i for i in s if i in "aeiouAEIOU"]
        result=[i if i not in "aeiouAEIOU" else vowels.pop() for i in s]
        return "".join(result)

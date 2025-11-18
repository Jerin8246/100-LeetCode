class Solution:
    def lengthOfLongestSubstring(self, s: str)->int:
        left = 0
        n = len(s)
        maxlength = 0
        charSet = set()
        length = 0
        
        for right in range(n):
            if s[right] not in charSet:
                charSet.add(s[right])
                length +=1
                maxlength = max( maxlength , length)
            else:
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left += 1
                charSet.add(s[right])
                length = right - left + 1 
            
    
        return   maxlength

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         length = 0
#         left = 0
#         charSet = set()

#         for right in range(len(s)):
#             while s[right] in charSet:
#                 charSet.remove(s[left])
#                 left += 1

                
#             length = max(length,  right - left + 1)
#             charSet.add(s[right])
        
#         return length
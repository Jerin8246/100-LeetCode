# #My method:

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         my_chars1 = []
#         my_chars2 = []
#         s = s.lower()
#         for i in s:
#             if i.isalnum():
#                 my_chars1.append(i)
#         for i in s[::-1]: #reverse string using slice notation     
#             if i.isalnum():
#                 my_chars2.append(i)
        
#         if(my_chars1 == my_chars2):
#             return True
#         else:
#             return False


# Provided solution

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         left , right = 0 , len(s) -1
#         s = s.lower()

#         while left < right:
#             if not s[left].isalnum():
#                 left += 1
      
#             if not s[right].isalnum():
#                 right -= 1
            
#             if s[left].isalnum() and s[right].isalnum():
#                 if s[left] != s[right]:
#                     return False
                
#                 left += 1
#                 right -= 1
            
#         return True



class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        s= s.lower()
        for c in s:
            if c.isalnum():
                newStr += c
        
        left = 0
        right = len(newStr) - 1

        while left < right:
            if newStr[left] != newStr[right]:
                return False
            left += 1
            right -= 1
        
        return True


            

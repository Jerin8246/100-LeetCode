# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         word3 = ''
#         maxlen = max(len(word1), len(word2))
#         for i in range(maxlen):
#             if len(word1) > i:
#                 word3 += word1[i]
#             if len(word2) > i:
#                 word3 += word2[i]

#         return word3

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        min_len = min(len(word1), len(word2))

        for i in range(min_len):
            result += word1[i] + word2[i]

        if len(word1) > len(word2):
            result += word1[min_len:]
        else:
            result += word2[min_len:]
            
        return result
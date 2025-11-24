# #   My_solution

# class Solution:
#     def wordPattern(self, pattern: str, s: str) -> bool:
#         words = s.split()
#         my_dict = dict()

#         if len(words) != len(pattern):
#             return False
        
#         for i in range(len(pattern)):
#             if pattern[i]  in my_dict:
#                 if my_dict[pattern[i]] != words[i]:
#                     return False
#             else:
#                 if words[i]  in my_dict.values():
#                     return False
#                 else:
#                     my_dict[pattern[i]] = words[i]

#         return True

# #   Provided Solution
# class Solution:
#     def wordPattern(self, pattern: str, s: str) -> bool:
#         words = s.split()

#         if len(words) != len(pattern):
#             return False
        
#         pattern_to_words = {}
#         words_to_pattern = {}

#         for i in range(len(pattern)):
#             p = pattern[i]
#             w = words[i]

#             if p in pattern_to_words and pattern_to_words[p] != w:
#                 return False
#             if w in words_to_pattern and words_to_pattern[w] != p:
#                 return False
#             pattern_to_words[p] = w
#             words_to_pattern[w] = p
        
#         return True


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        let_in_pattern = {}
        words_in_pattern = {}

        t = s.split()

        if len(t) != len(pattern):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in let_in_pattern:
                let_in_pattern[pattern[i]] = i
            if t[i] not in words_in_pattern:
                words_in_pattern[t[i]] = i
            if words_in_pattern[t[i]] != let_in_pattern[pattern[i]]:
                return False
        
        return True
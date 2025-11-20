class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        my_dict = {}
        
        # Populate the dictionary with characters from the magazine
        # my_dict.get(i, 0):
        # It looks for the key i inside my_dict.
        # If the key exists: It returns the current value associated with i.
        # If the key does NOT exist: It returns the default value, which is specified here as 0.

        for i in magazine:
            my_dict[i] = my_dict.get(i, 0) + 1
        
        # Check if ransomNote can be constructed
        for i in ransomNote:
            my_key = my_dict.get(i, 0)
            if my_key == 0:
                return False
            my_dict[i] -= 1
        
        return True




# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:

#         ran, mag = Counter(ransomNote), Counter(magazine)
#         if ran & mag == ran:  # & = intersection
#             return True
#         return False



# # Below I am explaining how Counter works
# # #from collections import Counter

# # string_counter = Counter("hello")
# # print(string_counter)
# # # Output: Counter({'h': 1, 'e': 1, 'l': 2, 'o': 1})


# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         my_dict = {}

#         for i in magazine:
#             my_dict[i] = my_dict.get(i, 0) + 1
        
#         for i in ransomNote:
#             my_dict[i] = my_dict.get(i, 0 ) - 1
#             if my_dict[i] == -1:
#                 return False
        
#         return True
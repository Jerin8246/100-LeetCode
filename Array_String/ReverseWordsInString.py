# # 151. Reverse Words in a String
# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

# Example 1:

# Input: s = "the sky is blue"
# Output: "blue is sky the"
# Example 2:

# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:

# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.


class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()  # splits and removes extra spaces
        result = [i for i in reversed(words)]  # or: words[::-1]
        return ' '.join(result)  # join with space between words


class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        result = [words.pop() for _ in range(len(words))]
        return ' '.join(result)      # The  space in inserted between each element in list as a glue



class Solution:
    def reverseWords(self, s: str) -> str:
        word = s.split()
        if s == '':
            return  ''
        result = ''
        i = len(word) - 1
        while i > 0:
            result += word[i]
            result += ' '
            i -= 1
        result += word[0]
        return  result
            
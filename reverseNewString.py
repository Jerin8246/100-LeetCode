class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        new_str = ""
        for i in range(len(words)-1, 0, -1):
            new_str += words[i]
            new_str += " "
        new_str += words[0]
        return new_str
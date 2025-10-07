class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        result = s.split()
        lword = result[-1]
        return len(lword)
        
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = dict()

        for i in range(len(s)):
            if s[i] in d:
                if d[s[i]] != t[i]:
                    return False
            else:
                if t[i] not in d.values():
                    d[s[i]] = t[i]
                else:
                    return False

        return True
        
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_index_s = {}
        char_index_t = {}

        for i in range(len(s)):
            # Store the index of the first occurenece of each character in  s
            if s[i] not in char_index_s:
                char_index_s[s[i]] = i

            # Store the index of the first occurences of each character in t
            if t[i] not in char_index_t:
                char_index_t[t[i]] = i

            # For two strings to be isomorphic:
            # 👉 The first time we saw a character in s must match
            # 👉 The first time we saw the corresponding character in t
            if char_index_s[s[i]] != char_index_t[t[i]]:
                return False

        return True






        

        


            
# My Solution

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
                    
        d1, d2 = Counter(s), Counter(t)
        
        if d1 & d2 == d1:
            return True
        
        else: return False

# defaultdict(int) creates a defaultdict named count with a default value of 0 for any keys that are not yet present in the dictionary.

#preffered Solution
            
# class Solution: 
    def isAnagram(self, s: str, t: str) -> bool:
        count = defaultdict(int)

        for x in s:
            count[x] += 1
        
        for x in t:
            count[x] -= 1
        
        for val in count.values():
            if val != 0:
                return False
        
        return True


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        d = {}
        
        for i in s:
            d[i] = d.get(i, 0) + 1

        for i in t:
            d[i] = d.get(i, 0) - 1

        for i in d:
            if d[i] != 0:
                return False
        
        return True


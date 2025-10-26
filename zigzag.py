class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows == len(s):
            return s
        
        rows = [[] for _ in range(numRows)]
        idx, d = 0, 1

        for c in s:
            rows[idx].append(c)
            if idx == 0:
                d = 1
            if idx == numRows - 1:
                d = -1
            idx += d

        for i in range(numRows):
            rows[i] = ''.join(rows[i])
        
        return ''.join(rows)
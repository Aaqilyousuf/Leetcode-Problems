class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        i = 0
        n = len(s)
        res = []
        while i<n:
            j = i
            while j<n and s[j] == s[i]:
                j += 1
            if j-i>=3:
                res.append([i, j-1])
            i=j
        return res
            
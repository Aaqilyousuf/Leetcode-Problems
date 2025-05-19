class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        a = 0
        res = 0
        for i in range(len(s)):
            if s[i] == '(':
                a += 1
            elif a>0:
                a -= 1
            else:
                res += 1
        return res+a
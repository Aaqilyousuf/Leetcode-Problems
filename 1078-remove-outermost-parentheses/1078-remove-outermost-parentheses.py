class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        depth = 0
        res = ""
        for i in range(len(s)):
            if s[i] == "(":
                if depth>0:
                    res += s[i]
                depth += 1
            else:
                depth -= 1
                if depth > 0:
                    res += s[i]
        return res
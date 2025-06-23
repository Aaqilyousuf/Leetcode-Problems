class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        stack = []

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] ==")":
                if stack and s[stack[-1]] == "(":
                    stack.pop()
                else:
                    stack.append(i)
        res = []
        for i in range(len(s)-1, -1, -1):
            if stack and stack[-1] == i:
                stack.pop()
            else:
                res.append(s[i])
        ans = "".join(reversed(res))
        return ans

        

        
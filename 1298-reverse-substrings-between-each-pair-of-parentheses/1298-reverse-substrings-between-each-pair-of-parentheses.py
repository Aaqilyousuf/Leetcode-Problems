class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        stack = []

        for i in s:
            if i != ')':
                stack.append(i)
            else:
                new = []
                while stack and stack[-1] != '(':
                    new.append(stack.pop())
                stack.pop()
                stack.extend(new)
        
        return ''.join(stack)
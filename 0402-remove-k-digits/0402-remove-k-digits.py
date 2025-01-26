class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == len(num):
            return '0'
        stack = []
        for n in num:
            while stack and ord(stack[-1]) > ord(n) and k!=0:
                stack.pop()
                k -= 1

            stack.append(n)
        while k > 0:
            stack.pop()
            k -= 1
        while stack and stack[0] == '0':
            stack.pop(0)
        if not stack:
            return '0'
        return "".join(stack)
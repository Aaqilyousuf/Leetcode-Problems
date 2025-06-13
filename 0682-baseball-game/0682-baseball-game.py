class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == 'C' and stack:
                stack.pop()
            elif op == 'D' and stack:
                stack.append(stack[-1]*2)
            elif op == '+' and len(stack) >= 2:
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(op))
        res = 0
        for x in stack:
            res += x
        return res

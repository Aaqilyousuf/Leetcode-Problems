class Solution:
    def pivotInteger(self, n: int) -> int:
        tot = n*(n+1)//2
        for x in range(1, n+1):
            uptoX = x*(x+1)//2
            fromX = tot - (x-1)*x//2
            if uptoX == fromX:
                return x
        return -1
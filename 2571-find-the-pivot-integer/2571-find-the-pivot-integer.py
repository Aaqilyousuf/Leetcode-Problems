class Solution:
    def pivotInteger(self, n: int) -> int:
        tot = n*(n+1)//2
        for x in range(1, n+1):
            uptoX = x*(x+1)//2 #sum from 1 to x
            fromX = tot - (x-1)*x//2 # sum from x to n
            if uptoX == fromX: #if both matches then x is pivot integer
                return x
        return -1
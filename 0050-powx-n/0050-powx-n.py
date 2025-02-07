class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            x = 1/x
            n = -n
        return self.helper(x, n)
    def helper(self, x, n):
        if n==0:
            return 1
        if x==0:
            return 0
        res = self.helper(x, n//2)
        res *= res
        return res if n%2==0 else res*x
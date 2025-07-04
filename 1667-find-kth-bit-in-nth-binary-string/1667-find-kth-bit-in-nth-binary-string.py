class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def helper(n, k):
            if n == 1:
                return "0"
            mid = 2 ** (n - 1)
            if k == mid:
                return "1"
            elif k < mid:
                return helper(n - 1, k)
            else:
                mirror = 2 ** n - k
                bit = helper(n - 1, mirror)
                return "0" if bit == "1" else "1"

        return helper(n, k)

class Solution:
    def hammingWeight(self, n: int) -> int:
        # return (bin(n).count("1"))
        cnt = 0
        while n:
            cnt += n & 1
            n >>= 1
        return cnt
            
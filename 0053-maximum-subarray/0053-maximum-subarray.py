class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        maxi = float("-inf")
        for n in nums:
            s += n
            maxi = max(maxi, s)
            if s<0:
                s = 0
        return maxi

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0
        l, r = 0, 0
        zeroCount = 0
        while r<len(nums):
            if nums[r] == 0:
                zeroCount += 1
            while zeroCount > k:
                if nums[l] == 0:
                    zeroCount -= 1
                l += 1
            res = max(res, r-l+1)
            r += 1
        return res
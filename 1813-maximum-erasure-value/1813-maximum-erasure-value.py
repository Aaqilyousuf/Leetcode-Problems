class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = 0
        r = 0
        s = set()
        n = len(nums)
        res = 0
        curSum = 0
        for r in range(n):
            while nums[r] in s:
                s.remove(nums[l])
                curSum -= nums[l]
                l += 1
            s.add(nums[r])
            curSum += nums[r]
            res = max(res, curSum)
        return res
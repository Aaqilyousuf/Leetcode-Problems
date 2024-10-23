class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        a = nums[0]
        n = len(nums)
        res = 0
        for i in range(len(nums)):
            res += nums[i] - a
        return res

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm = {}
        nu = len(nums)
        maxRes = float("-inf")
        for n in nums:
            hm[n] = 1 + hm.get(n, 0)
            if hm[n] > nu//2:
                maxRes = max(maxRes, n)
        return maxRes

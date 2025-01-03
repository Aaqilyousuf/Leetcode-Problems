class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        #prefix and suffix sum problem
        tot = sum(nums)
        way = 0
        prefix = 0
        for i in range(len(nums) - 1):
            prefix += nums[i]
            suffix = tot - prefix
            if prefix >= suffix:
                way += 1
        return way
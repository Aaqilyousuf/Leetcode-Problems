class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        tot = 0
        for i in range(len(nums)):
            s = nums[i]
            l = nums[i]
            for j in range(i, len(nums)):
                s = min(s, nums[j])
                l = max(l, nums[j])
                tot += l - s
        return tot
        


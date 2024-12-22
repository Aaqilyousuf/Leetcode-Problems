class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        ind = -1
        large = float('-inf')
        for i in range(len(nums)):
            if nums[i] > large:
                large = nums[i]
                ind = i
        return ind
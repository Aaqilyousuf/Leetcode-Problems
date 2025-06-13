class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        maxDiff = float('-inf')

        for i in range(n*2-1):
            maxDiff = max(maxDiff, abs(nums[i%n]-nums[(i+1)%n]))
        return maxDiff

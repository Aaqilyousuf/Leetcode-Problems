class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxSum = -1
        minVal = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < minVal:
                minVal = nums[i]
            else:
                maxSum = max(maxSum, nums[i]-minVal)
        return -1 if maxSum==0 else maxSum
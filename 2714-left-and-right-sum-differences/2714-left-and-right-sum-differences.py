class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum = [0] * len(nums)
        rightSum = [0] * len(nums)
        for i in range(1, len(nums)):
            leftSum[i] = nums[i-1] + leftSum[i-1]
        for i in range(len(nums)-2, -1, -1):
            rightSum[i] = nums[i+1] + rightSum[i+1]
        ans = []
        for i in range(len(nums)):
            ans.append(abs(leftSum[i]- rightSum[i]))
        return ans
class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        maxEle = max(nums)

        maxSum = maxEle * k + (k*(k-1))//2
        return maxSum

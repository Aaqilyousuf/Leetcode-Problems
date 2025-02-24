class Solution:
    def rob(self, nums: List[int]) -> int:
        # n = len(nums)
        # dp = [0] * (n+1)
        # dp[1] = nums[0]
        # for i in range(2, n+1):
        #     if i<=n:
        #         dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
        # return dp[n]
        prev2, prev1 = 0, 0 
        for n in nums:
            curr = max(prev1, prev2+n)
            prev2, prev1 = prev1, curr
        return prev1
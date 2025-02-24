class Solution:
    def rob(self, nums: List[int]) -> int:
        def robber(nums):
            n = len(nums)
            dp = [0]*(n+1)
            dp[1] = nums[0]
            for i in range(2, n+1):
                dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])
            return dp[n]

        n = len(nums)
        if n==0:
            return 0
        if n==1:
            return nums[0]
        case1 = robber(nums[1:])
        case2 = robber(nums[:-1])
        res = max(case1, case2)
        return res
        
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # n=len(nums)
        # Sum=sum(nums)
        # diff=Sum-target

        # if diff<0 or diff%2==1: return 0
        # diff/=2
        
        # @cache
        # def f(j , sum):
        #     if j==0: return 1 if sum==0 else 0
        #     x=nums[j-1]
        #     ans=f(j-1, sum)
        #     if sum>=x:
        #         ans+=f(j-1, sum-x)
        #     return ans
        # return f(n, diff)
        memo = {}
        def backtrack(i, tot):
            if i==len(nums):
                return 1 if tot == target else 0
            if (i, tot) in memo:
                return memo[(i, tot)]
            memo[(i, tot)] = (backtrack(i+1, tot+nums[i]) + backtrack(i+1, tot-nums[i]))
            return memo[(i, tot)]
        return backtrack(0, 0)
       
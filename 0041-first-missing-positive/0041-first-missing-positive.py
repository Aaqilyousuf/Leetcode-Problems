class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i]<=0 or nums[i]>n: #as per condition 
                nums[i] = n+1
        for i in range(n):
            val = abs(nums[i])
            if val <= n:
                nums[val-1] = -abs(nums[val-1]) #marking the index of existing number
        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n+1
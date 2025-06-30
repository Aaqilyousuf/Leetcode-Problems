class Solution:
    def findLHS(self, nums: List[int]) -> int:
        #using sort
        nums.sort()
        j = 0
        maxLen = 0
        for i in range(len(nums)):
            while nums[i] - nums[j] > 1:
                j += 1
            if nums[i] - nums[j] == 1:
                maxLen = max(maxLen, i-j+1)
        return maxLen
            
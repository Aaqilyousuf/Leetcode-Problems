class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOne = 0
        cur = 0
        for i in nums:
            if i==1:
                cur += 1
                maxOne = max(maxOne, cur)
            else:
                cur = 0
        return maxOne
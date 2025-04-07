class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        start = []
        for i in range(len(nums)):
            s = max(0, i-nums[i])
            start.append(s)
        tot = 0
        for i in range(len(start)):
            tot += sum(nums[start[i]:i+1])
        return tot
        
        
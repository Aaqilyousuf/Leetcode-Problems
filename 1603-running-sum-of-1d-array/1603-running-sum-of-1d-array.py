class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefixSum = [nums[0]]

        for i in range(1, len(nums)):
            cur = nums[i]
            prefix = prefixSum[-1]
            prefixSum.append(cur + prefix)
        return prefixSum
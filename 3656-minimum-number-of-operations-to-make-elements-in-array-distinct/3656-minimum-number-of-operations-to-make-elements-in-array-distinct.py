class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        if len(nums) == len(set(nums)):
            return 0
        operation = 0
        while len(nums) > len(set(nums)):
            nums = nums[3:]
            operation += 1
        return operation

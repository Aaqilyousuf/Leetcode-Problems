class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        a = l*(l+1) // 2
        sumof = sum(nums)
        return a-sumof

        
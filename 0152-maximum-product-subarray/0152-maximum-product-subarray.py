class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        a = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                a = 1
                res = max(res, 0)
                continue
            a *= nums[i]
            res = max(res, a)
        a = 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 0:
                a = 1
                res = max(res, 0)
                continue
            a *= nums[i]
            res = max(res, a)
        return res        
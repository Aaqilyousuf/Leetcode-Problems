class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        if 0 not in nums:
            return 0
        res = 0
        cnt = 0
        for num in nums:
            if num == 0:
                cnt += 1
                res += cnt
            else:
                cnt = 0
        return res

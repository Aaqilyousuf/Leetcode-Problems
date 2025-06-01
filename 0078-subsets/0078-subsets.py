class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        tot = 1 << n
        res = []

        for mask in range(tot):
            sub = []
            for i in range(n):
                if mask & (1 << i):
                    sub.append(nums[i])
            res.append(sub)
        return res
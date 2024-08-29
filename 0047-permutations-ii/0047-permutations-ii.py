class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        res = []
        for i in range(len(nums)):
            n = nums[i]
            r = nums[:i] + nums[i+1:]
            for b in self.permuteUnique(r):
                res.append([n] + b)

        result = list(map(list, set(map(tuple, res))))

        return result
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []
        self.backtrack(0, nums, res, sol)
        return res
    def backtrack(self, i , nums, res, sol):
        if i == len(nums):
            res.append(sol[:])
            return
        self.backtrack(i+1, nums, res, sol)
        sol.append(nums[i])
        self.backtrack(i+1, nums, res, sol)
        sol.pop() #backtrack
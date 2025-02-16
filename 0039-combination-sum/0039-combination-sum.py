class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(start, nums, tot):
            if tot == target:
                res.append(nums[:])
                return
            if tot > target:
                return
            for i in range(start, len(candidates)):
                nums.append(candidates[i])
                backtrack(i, nums, tot+candidates[i])
                nums.pop()
                # backtrack(start+1, nums)
            
        backtrack(0, [], 0)
        return res

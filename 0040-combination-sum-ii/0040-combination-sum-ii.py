class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(start, nums, tot):
            if tot == target:
                res.append(nums[:])
                return
            for i in range(start, len(candidates)):
                if i>start and candidates[i] == candidates[i-1]:
                    continue
                if tot+candidates[i] > target:
                    break
                dfs(i+1, nums+[candidates[i]], tot+candidates[i])
        dfs(0,[], 0)
        return res
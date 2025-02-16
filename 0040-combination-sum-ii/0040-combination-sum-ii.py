class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(start, nums, target):
            if target<0:
                return
            if target == 0:
                res.append(nums[:])
            for i in range(start, len(candidates)):
                if i>start and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > target:
                    break
                dfs(i+1, nums+[candidates[i]], target-candidates[i])
        dfs(0,[], target)
        return res
class Solution:
    def combinationSum3(self, k: int, n: int, start = 1) -> List[List[int]]:
        # nums = [i for i in range(1, 10)]
        # combo = itertools.combinations(nums, k)
        # res = [i for i in combo if sum(i)==n]
        # return res
        res = []
        def dfs(start, nums, tot):
            if len(nums)==k:
                if tot==n:
                    res.append(nums[:])
                return
            for i in range(start, 10):
                if tot+i>n:
                    break
                dfs(i+1, nums+[i], tot+i)
        dfs(1, [], 0)
        return res

            
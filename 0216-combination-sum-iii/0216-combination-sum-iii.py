class Solution:
    def combinationSum3(self, k: int, n: int, start = 1) -> List[List[int]]:
        nums = [i for i in range(1, 10)]
        combo = itertools.combinations(nums, k)
        res = [i for i in combo if sum(i)==n]
        return res

            
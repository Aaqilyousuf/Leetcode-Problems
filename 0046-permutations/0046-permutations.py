class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # per = permutations(nums)
        # res1 = list(per)
        # return res1
        n = len(nums)
        ans, sol = [], []

        def backtrack():
            if len(sol) == n:
                ans.append(sol[:])
                return 
            for x in nums:
                if x not in sol:
                    sol.append(x)
                    backtrack()
                    sol.pop()
        backtrack()
        return ans

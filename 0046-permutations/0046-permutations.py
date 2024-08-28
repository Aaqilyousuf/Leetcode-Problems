class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        per = permutations(nums)
        res1 = list(per)
        return res1
        res = []
        # l = len(nums)
        # for i in range(l):
        #     if nums not in res:
        #         res.append(nums)
            

        
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        uniqueEle = sorted(set(arr))
        rankMap = {}
        rank = 1
        for i, n in enumerate(uniqueEle):
            rankMap[n] = rank+i
        res = []
        for n in arr:
            res.append(rankMap[n])
        return res




        
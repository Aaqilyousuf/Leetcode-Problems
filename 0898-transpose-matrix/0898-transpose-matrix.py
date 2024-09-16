class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = []
        l = len(matrix[0])
        for i in range(l):
            res.append([m[i] for m in matrix])
        return res
        
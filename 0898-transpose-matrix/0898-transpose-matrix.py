class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        l = len(matrix[0])
        res = []
        for i in range(l):
            dum = []
            for m in matrix:
                dum.append(m[i])
            res.append(dum)
        return res
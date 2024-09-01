class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        l = len(original)
        res = []
        if l == m*n:
            for i in range(0, l, n):
                sublist = original[i: i+n]
                res.append(sublist)
        return res
           
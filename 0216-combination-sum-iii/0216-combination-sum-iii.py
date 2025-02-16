class Solution:
    def combinationSum3(self, k: int, n: int, start = 1) -> List[List[int]]:
        if k == 1:
            if start <= n <=9:
                return [[n]]
            else:
                return []
        res = []
        for i in range(start,9):
            tmp = self.combinationSum3(k-1,n-i,i+1)
            for j in tmp:
                j.insert(0,i)
                res.append(j)
        return res

            
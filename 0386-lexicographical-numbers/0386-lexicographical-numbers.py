class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        if n < 10:
            return [x for x in range(1, n+1)]
        res = []
        cur = 1
        for i in range(n):
            res.append(cur)
            if cur*10 <= n:
                cur *= 10
            elif cur % 10 != 9 and cur+1 <= n:
                cur += 1
            else:
                while cur % 10 == 9 or cur+1 > n:
                    cur //= 10
                cur += 1
        return res
                

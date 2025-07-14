class Solution:
    def countBits(self, n: int) -> List[int]:
        def helper(i):
            b = str(bin(i))
            idk = b[2:]
            cnt = 0
            for i in idk:
                if i=="1":
                    cnt += 1
            res.append(cnt)
        res = []
        for i in range(n+1):
            helper(i)
        return res
     

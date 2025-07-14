class Solution:
    def countBits(self, n: int) -> List[int]:
        # def helper(i):
        #     b = str(bin(i))
        #     idk = b[2:]
        #     cnt = 0
        #     for i in idk:
        #         if i=="1":
        #             cnt += 1
        #     res.append(cnt)
        # res = []
        # for i in range(n+1):
        #     helper(i)
        # return res
        dp = [0] * (n + 1)
        for i in range(1, n+1):
            dp[i] = dp[i>>1] + (i&1)
        return dp
     

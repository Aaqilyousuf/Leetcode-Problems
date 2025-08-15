class Solution:
    def longestPalindrome(self, s: str) -> str:
        # res = ""
        # resLen = 0
        # for i in range(len(s)):
        #     #odd
        #     l, r = i, i
        #     while l>=0 and r<len(s) and s[l] == s[r]:
        #         if resLen < r-l+1:
        #             res = s[l:r+1]
        #             resLen = r-l+1
        #         l-=1
        #         r += 1
        #     #even
        #     l, r = i, i+1
        #     while l>=0 and r<len(s) and s[l]==s[r]:
        #         if resLen < r-l+1:
        #             res = s[l:r+1]
        #             resLen = r-l+1
        #         l -= 1
        #         r += 1
        # return res
        #2D DP
        n = len(s)
        if n < 2:
            return s
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        start, maxL = 0 ,1
        for l in range(2, n+1):
            for i in range(n-l+1):
                j = i+l-1
                if s[i] == s[j]:
                    if l == 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = False
                
                if dp[i][j] and l > maxL:
                    start = i
                    maxL = l
        return s[start:start+maxL]

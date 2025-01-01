class Solution:
    def maxScore(self, s: str) -> int:
        res = -1
        for i in range(1, len(s)):
            left = s[:i]
            right = s[i:]

            lsum = 0
            for a in left:
                if a == "0":
                    lsum += 1
            rsum = 0
            for a in right:
                if a == "1":
                    rsum += 1
            tot = lsum + rsum
            res = max(res, tot)
        return res
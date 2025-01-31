class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cmap = {}
        res = 0
        maxFreq = 0
        l = 0
        for r in range(len(s)):
            cmap[s[r]] = 1 + cmap.get(s[r], 0)
            maxFreq = max(maxFreq, cmap[s[r]])

            while (r-l+1) - maxFreq > k:
                cmap[s[l]] -= 1
                l += 1

            res = max(res, r-l+1)
        return res
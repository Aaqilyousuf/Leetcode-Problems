class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(n):
            freq = defaultdict(int)
            for j in s[i:]:
                freq[j] += 1
                vals = freq.values()
                res += max(vals) - min(vals)
        return res
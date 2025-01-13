class Solution:
    def minimumLength(self, s: str) -> int:
        freq = [0] * 26
        tot = 0
        for i in range(len(s)):
            freq[ord(s[i]) - ord("a")] += 1
        for f in freq:
            if f == 0:
                continue
            if f % 2 == 0:
                tot += 2
            else:
                tot += 1
        return tot

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hmap = {}
        for c in s:
            hmap[c] = hmap.get(c, 0) + 1
        for i in range(len(s)):
            if hmap[s[i]] == 1:
                return i
        return -1
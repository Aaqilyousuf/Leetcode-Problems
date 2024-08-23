class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # if needle not in haystack:
        #     return -1
        # else:
        #     return 0
        r = len(needle)
        l = 0
        while len(haystack) > l:
            if haystack[l:r] == needle:
                ind = l
                return ind
            l += 1
            r += 1
        return -1
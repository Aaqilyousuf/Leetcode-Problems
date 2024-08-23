class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a = strs[0]
        for i in strs[1:]:
            while not i.startswith(a):
                a = a[:-1]
                if not a:
                    return ""
        return a
        
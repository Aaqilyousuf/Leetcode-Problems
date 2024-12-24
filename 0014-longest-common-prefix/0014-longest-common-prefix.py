class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = strs[0]
        for i in strs[1:]:
            while not i.startswith(s):
                s = s[:-1]
                if not s:
                    return ""
        return s
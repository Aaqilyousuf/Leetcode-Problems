class Solution:
    def countSubstrings(self, s: str) -> int:
        def helper(left, right):
            count = 0
            while left>=0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count
        tot = 0
        for i in range(len(s)):
            tot += helper(i,i)
            tot += helper(i, i+1)
        return tot
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash = {}
        res = []
        for char in s:
            if char not in hash:
                hash[char] = 1
            else:
                hash[char] += 1
        for i in range(len(s)):
            if hash[s[i]] == 1:
                return i
        return -1
        
        
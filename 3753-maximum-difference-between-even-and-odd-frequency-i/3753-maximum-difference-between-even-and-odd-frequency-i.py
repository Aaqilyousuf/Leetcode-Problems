class Solution:
    def maxDifference(self, s: str) -> int:
        hashMap = {}
        for ch in s:
            hashMap[ch] = 1 + hashMap.get(ch, 0)
        maxDiff = float('-inf')
        oddMax = float('-inf')
        evenMin = float('inf')
        for ch in hashMap:
            if hashMap[ch] % 2 != 0:
                oddMax = max(oddMax, hashMap[ch])
            else:
                evenMin = min(evenMin, hashMap[ch])
        res = oddMax - evenMin
        return res
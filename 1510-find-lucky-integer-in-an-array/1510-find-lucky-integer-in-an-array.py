class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freqMap = defaultdict(int)
        for n in arr:
            freqMap[n] += 1
        mx = -1
        for n in freqMap:
            if freqMap[n] == n:
                mx = max(mx, n)
        return mx 
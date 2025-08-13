class Solution:
    def frequencySort(self, s: str) -> str:
        freqMap = defaultdict(int)
        for ch in s:
            freqMap[ch] += 1
        freqList = []
        for k, v in freqMap.items():
            freqList.append((k, v))
        sortedFreq = sorted(freqList, key=lambda x:x[1], reverse=True)
        res = ""
        for k, v in sortedFreq:
            res += k*v
        return res
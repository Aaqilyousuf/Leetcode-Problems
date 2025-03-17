class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
        maxF = max(freq.values())
        res = 0
        for k, v in freq.items():
            if v==maxF:
                res+=v
        return res
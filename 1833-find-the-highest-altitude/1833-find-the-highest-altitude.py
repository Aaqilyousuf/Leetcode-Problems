class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix = [0] * (len(gain)+1)
        for i in range(1, len(gain)+1):
            prefix[i] = gain[i-1] + prefix[i-1]
        res = max(prefix)
        return res

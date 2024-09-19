class Solution:
    def minPartitions(self, n: str) -> int:
        larger = int(n[0])
        for s in n:
            larger = max(larger, int(s))
        return larger
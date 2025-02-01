class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        lsum, rsum, maxsum = 0, 0, 0
        n = len(cardPoints)
        for i in range(k):
            lsum += cardPoints[i]
        maxsum = lsum
        rind = n-1
        for i in range(k-1, -1, -1):
            lsum -= cardPoints[i]
            rsum += cardPoints[rind]
            rind -= 1
            maxsum = max(maxsum, lsum + rsum)
        return maxsum
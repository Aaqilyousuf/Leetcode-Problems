class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        res = high
        while low<=high:
            k = low+(high-low)//2
            hrs = 0
            for p in piles:
                hrs += math.ceil(p/k)
            if hrs<=h:
                res = min(res, k)
                high = k - 1
            else:
                low = k+1
        return res

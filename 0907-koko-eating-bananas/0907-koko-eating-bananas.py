class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        res = high
        while low<=high:
            mid = (low+high) // 2
            k = 0
            for p in piles:
                k += math.ceil(p/mid)
            if k <= h:
                res = min(res, mid)
                high = mid - 1
            else:
                low = mid + 1
        return res

        

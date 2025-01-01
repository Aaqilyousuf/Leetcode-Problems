class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low, high = max(weights), sum(weights)
        res = -1
        while low <= high:
            mid = low + (high-low)//2
            if self.findPossible(weights, mid, days):
                res = mid #one of possible ans
                high = mid - 1 #why because we need least so we need to find in rightside
            else:
                low = mid + 1
        return res
    def findPossible(self, weights, mid, d):
        days = 1
        load = 0
        #here mid is one of possible capacity
        for i in range(len(weights)):
            if load + weights[i] > mid:
                 days += 1
                 load = weights[i]
            else:
                load += weights[i]
        if days> d:
            return False
        return True
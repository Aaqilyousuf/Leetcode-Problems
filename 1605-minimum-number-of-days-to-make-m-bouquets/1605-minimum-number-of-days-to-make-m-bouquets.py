class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        low = min(bloomDay)
        high = max(bloomDay)
        res = high
        while low<=high:
            mid = (low+high) // 2
            if self.findPossible(bloomDay, mid, k, m):
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res
    def findPossible(self, bloomDay, mid, k, m):
        noBouqets = 0
        cnt = 0
        for i in range(len(bloomDay)):
            if bloomDay[i] <= mid:
                cnt += 1
            else:
                noBouqets += cnt // k
                cnt = 0
        noBouqets += cnt // k
        if noBouqets >= m:
            return True
        return False
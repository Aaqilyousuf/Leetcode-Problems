class Solution:
    def arrangeCoins(self, n: int) -> int:
        # low, high = 0, n

        # while low<=high:
        #     mid = (low+high) // 2
        #     conis_needed = mid*(mid+1) // 2
        #     if conis_needed == n:
        #         return mid
        #     if conis_needed < n:
        #         low = mid + 1
        #     else:
        #         high = mid - 1
        # return high
        i = 1
        while i<=n:
            n -= i
            i += 1
        return i-1
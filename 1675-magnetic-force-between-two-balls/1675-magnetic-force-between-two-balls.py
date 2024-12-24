class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()
        low = 1
        high = position[n-1] - position[0]
        ans = -1
        while low<=high:
            mid = low + (high-low)//2
            if self.canWePlace(position, mid, m):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
    def canWePlace(self, pos, mid, m):
        cntBall = 1
        sum = pos[0]
        for i in range(1, len(pos)):
            if pos[i] - sum >= mid:
                cntBall += 1
                sum = pos[i]
            if cntBall >= m:
                return True
        return False


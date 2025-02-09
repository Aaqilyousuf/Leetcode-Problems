class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()
        l, r = 1, position[-1] - position[0]
        best = -1
        while l<=r:
            mid = (l+r)//2
            if self.helper(position, mid, m):
                best = mid
                l = mid+1
            else:
                r = mid-1
        return best
    def helper(self, nums, maxT, m):
        balls = 1
        sumPos = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - sumPos >= maxT:
                balls += 1
                sumPos = nums[i]
                if balls == m:
                    return True
        return False

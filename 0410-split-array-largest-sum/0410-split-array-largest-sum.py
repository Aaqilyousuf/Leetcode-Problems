class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low = min(nums)
        high = sum(nums)
        res = -1
        while low<=high:
            mid = low + (high-low)//2

            if self.findPossible(nums, mid, k):
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res
    def findPossible(self, nums, mid, k):
        s = 1
        p = 0

        for i in range(len(nums)):
            if nums[i] > mid:
                return False
            if p + nums[i] > mid:
                s += 1
                p = nums[i]
            else:
                p += nums[i]
        if s > k:
            return False
        return True

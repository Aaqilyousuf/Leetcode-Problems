class Solution:
    def searchRange(self, nums, target):
        left = self.binSearch(nums, target, True)
        right = self.binSearch(nums, target, False)
        return [left, right]
    def binSearch(self, nums, target, leftbias):
        l, r = 0, len(nums) - 1
        i = -1
        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                i = m
                if leftbias:
                    r = m-1
                else:
                    l = m+1
                continue
            if nums[m] < target:
                l = m+1
            else:
                r = m-1
        return i
       
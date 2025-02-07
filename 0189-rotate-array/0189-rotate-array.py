class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # def reverse(l, r):
        #     while l<r:
        #         nums[l], nums[r] = nums[r], nums[l]
        #         l += 1
        #         r -= 1

        # norm = k % len(nums)
        # if norm == 0:
        #     return
        # reverse(0, len(nums)-1)
        # reverse(0, norm-1)
        # reverse(norm, len(nums) - 1)
        k = k % len(nums)
        if k == 0:
            return nums
        nums[:] = nums[-k:] + nums[:-k]
        
        
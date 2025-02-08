
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 1
        lastInc = -1
        while i<n:
            if nums[i] > nums[i-1]:
                lastInc = i
            i += 1
        if lastInc == -1:
            nums.reverse()
            return
      
        index = lastInc
        for i in range(lastInc, n):
            if nums[i] > nums[lastInc - 1] and nums[i] <= nums[index]:
                index = i
        nums[lastInc-1], nums[index] = nums[index], nums[lastInc-1]
        
        nums[lastInc:] = reversed(nums[lastInc:])
        
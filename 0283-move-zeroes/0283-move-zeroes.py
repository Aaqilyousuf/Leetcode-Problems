class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # l = 0
        # for r in range(1, len(nums)):
        #     if nums[l] == 0:
        #         nums[l], nums[r] = nums[r], nums[l]
        #         l += 1
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == 0:
        #             nums[i], nums[j] = nums[j], nums[i]

        l = 0  
        for r in range(len(nums)):  
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1  

        
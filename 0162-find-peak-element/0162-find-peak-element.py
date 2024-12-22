class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # Brute-force approach (commented out):
        # ind = -1
        # large = float('-inf')
        # for i in range(len(nums)):
        #     if nums[i] > large:
        #         large = nums[i]
        #         ind = i
        # return ind

        n = len(nums)  

        
        if n == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[n - 1] > nums[n - 2]:
            return n - 1

        low = 1
        high = n - 2
        while low <= high:
            mid = (low + high) // 2

            # If nums[mid] is the peak:
            if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
                return mid

            # If we are in the left:
            if nums[mid] > nums[mid - 1]:
                low = mid + 1

            # If we are in the right:
            else:
                high = mid - 1

        
        return -1

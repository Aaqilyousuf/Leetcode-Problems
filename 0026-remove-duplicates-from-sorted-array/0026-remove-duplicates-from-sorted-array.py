class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        slow = 0
        for fast in range(1, n):
            if nums[fast] != nums[slow]:
                 slow+=1
                 nums[slow] = nums[fast]
        return slow+1
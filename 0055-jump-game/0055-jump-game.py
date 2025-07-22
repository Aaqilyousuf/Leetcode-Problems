class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        if not nums:
            return False
        jump = 0
        for i in range(len(nums)):
            if i>jump:
                return False
            jump = max(jump, nums[i]+i) #current element + index gives the farthest index we can reach from i
            if jump >= len(nums)-1:
                return True
            
        return False
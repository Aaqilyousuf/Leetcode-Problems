class Solution:
    def jump(self, nums: List[int]) -> int:
       
        count = 0
        jump = 0
        curInd = 0
        for i in range(len(nums)-1):
            jump = max(jump, nums[i]+i)
            if i==curInd:
                count += 1
                curInd = jump
        return count
         
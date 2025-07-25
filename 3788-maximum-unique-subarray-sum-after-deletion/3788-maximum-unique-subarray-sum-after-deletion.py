class Solution:
    def maxSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        stack = []
        
        for i in range(len(nums)):
            if stack and nums[i] in stack:
                stack.remove(nums[i])

                
            if nums[i] < 0:
                continue
            stack.append(nums[i])
        if not stack:
            for n in nums:
                stack.append(n)
            return max(stack)
        print(stack)
        return sum(stack)
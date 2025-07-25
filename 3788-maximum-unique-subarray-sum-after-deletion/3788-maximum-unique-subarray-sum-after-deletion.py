class Solution:
    def maxSum(self, nums: List[int]) -> int:
        #worst time O(n2)
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
        #this fails
        # seen = set()
        # l = 0
        # curSum = 0
        # maxSum = nums[0]
        # for r in range(len(nums)):
        #     while nums[r] in seen:
        #         seen.remove(nums[l])
        #         curSum -= nums[l]
        #         l += 1

        #     seen.add(nums[r])
        #     curSum += nums[r]
        #     maxSum = max(maxSum, curSum)
        #     if curSum < 0:
        #         seen.clear()
        #         curSum = 0
        #         l = r + 1
        # return maxSum
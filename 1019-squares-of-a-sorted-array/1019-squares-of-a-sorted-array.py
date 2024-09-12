class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # res = []
        # a = [abs(num) for num in nums]
        # a.sort()
        # for n in a:
        #     res.append(n*n)
        # return res
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]
        nums.sort()
        return nums
        
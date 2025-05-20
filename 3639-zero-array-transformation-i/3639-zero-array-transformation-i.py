class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        #bruteforce
        # def helper(nums, l, r):
        #     for i in range(l, r+1):
        #         if nums[i] != 0:
        #             nums[i] -= 1
                    
        # n = len(nums)
        # for query in queries:
        #     l, r = query
        #     helper(nums, l, r)
        # zeroCount = 0
        # for i in nums:
        #     if i==0:
        #         zeroCount += 1
        # if zeroCount == n:
        #     return True
        # return False
        #Difference array technique
        n = len(nums)
        diff = [0] * (n+1)
        for l, r in queries:
            diff[l] -= 1
            if r+1<len(diff):
                diff[r+1] += 1
        curr = 0
        for i in range(n):
            curr += diff[i]
            nums[i] += curr
            if nums[i] < 0:
                nums[i] = 0
        return all(i==0 for i in nums)

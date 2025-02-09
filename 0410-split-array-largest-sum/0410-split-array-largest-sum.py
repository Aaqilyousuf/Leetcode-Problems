class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def helper(nums, maxT):
            split = 1
            sum = 0
            for n in nums:
                if n+sum > maxT:
                    split += 1
                    sum = n
                    if split > k:
                        return False
                else:
                    sum += n
            return True
        l = max(nums)
        r = sum(nums)
        while l<=r:
            m = l+(r-l)//2
            if helper(nums, m):
                r = m-1
            else:
                l = m+1
        return l
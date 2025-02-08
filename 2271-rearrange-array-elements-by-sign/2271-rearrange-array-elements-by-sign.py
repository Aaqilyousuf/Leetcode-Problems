class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        i = 0
        j = 1
        n = len(nums)
        res = [0] * len(nums)
        for num in nums:
            if num>0:
                if i<n:
                    res[i] = num
                    i+=2
            else:
                if j<n:
                    res[j] = num
                    j += 2
        return res

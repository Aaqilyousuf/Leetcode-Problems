class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low, high = 1, max(nums)
        res = high
        while low<=high:
            mid = (low+high)//2
            check = 0
            for n in nums:
                check += math.ceil(n/mid)
            if check<=threshold:
                res = min(res, mid)
                high = mid-1
            else:
                low = mid+1
        return res

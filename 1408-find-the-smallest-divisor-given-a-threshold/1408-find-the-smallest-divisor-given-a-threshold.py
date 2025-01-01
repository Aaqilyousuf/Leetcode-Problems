class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        #this problem is similar as koko eating bananas
        low = 1
        high = max(nums)
        res = high
        while low<=high:
            divisor = (low+high)//2
            divisorSum = 0
            for i in nums:
                divisorSum += math.ceil(i/divisor)
            if divisorSum <= threshold:
                res = min(res, divisor)
                high = divisor - 1
            else:
                low = divisor + 1
        return res


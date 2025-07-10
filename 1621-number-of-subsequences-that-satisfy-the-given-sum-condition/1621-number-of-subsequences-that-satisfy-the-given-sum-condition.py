class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)
        power = [1] * n

        for i in range(1, n):
            power[i] = (power[i-1] * 2)%MOD 
        l = 0
        r = n-1
        count = 0
        while l<=r:
            if nums[l] + nums[r] <= target:
                count = (count + power[r-l]) % MOD
                l += 1
            else:
                r -= 1
        return count



class Solution:
    def helper(self, nums: List[int], k: int) -> int:
        l = 0
        num_map = defaultdict(int)
        cnt = 0
        for r in range(len(nums)):
            num_map[nums[r]] += 1
            while len(num_map) > k:
                num_map[nums[l]] -= 1
                if num_map[nums[l]] == 0:
                    del num_map[nums[l]]
                l += 1
            cnt += (r-l+1)
        return cnt
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        res = self.helper(nums, k) - self.helper(nums, k-1)
        return res
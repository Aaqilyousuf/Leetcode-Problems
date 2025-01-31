class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        cur, prev = 0, 0
        ans = 0
        for i in nums:
            if i == 1:
                cur += 1
            else:
                ans = max(ans, cur+prev)
                prev = cur
                cur = 0
        ans = max(ans, cur+prev)
        return ans if ans != len(nums) else ans-1
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor_res = start ^ goal
        ans = 0
        while xor_res > 0:
            ans += xor_res & 1
            xor_res = xor_res >> 1
        return ans

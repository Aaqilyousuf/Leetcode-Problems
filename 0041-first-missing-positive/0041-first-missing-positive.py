class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        small = 1

        for n in nums:
            if small == n:
                small += 1
        return small
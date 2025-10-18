class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # xor = 0
        # for i in range(len(nums)):
        #     xor = xor ^ nums[i]
        # return xor
        if len(nums) == 1:
            return nums[0]
        mp = defaultdict(int)
        for n in nums:
            mp[n] += 1
        for n in mp:
            if mp[n] == 1:
                return n
        return -1
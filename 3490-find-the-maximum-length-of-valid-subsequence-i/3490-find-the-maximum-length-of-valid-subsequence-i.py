class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        #MY APPROACH
        # checkRes = []
        # for i in range(1, len(nums)):
        #     checkRes.append((nums[i-1] + nums[i]) % 2)
        # print(checkRes)
        # one = 0
        # zero = 0
        # for n in checkRes:
        #     if n == 1:
        #         one += 1
        #     else:
        #         zero += 1
        # res = max(one, zero) + 1
        # return res
        count_even = 0
        count_odd = 0
        for num in nums:
            if num % 2 == 0:
                count_even += 1
            else:
                count_odd += 1
        
        even_dp = 0
        odd_dp = 0
        for num in nums:
            if num % 2 == 0:
                even_dp = max(even_dp, odd_dp + 1)
            else:
                odd_dp = max(odd_dp, even_dp + 1)
        
        return max(count_even, count_odd, even_dp, odd_dp)
from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0] = 1 
        curr_sum = 0
        count = 0

        for num in nums:
            curr_sum += num  
            if (curr_sum - goal) in prefix_count:
                count += prefix_count[curr_sum - goal]

            prefix_count[curr_sum] += 1

        return count

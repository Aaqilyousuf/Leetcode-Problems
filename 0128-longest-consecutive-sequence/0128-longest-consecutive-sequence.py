class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        num_set = set(nums)
        longestCout = 0
        count = 0
        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                count = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    count += 1 
            longestCout = max(longestCout, count)  
        return longestCout
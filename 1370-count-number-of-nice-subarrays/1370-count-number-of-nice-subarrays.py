class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        cur_sum = 0
        count = 0
        for num in nums:
            cur_sum += 1 if num%2!=0 else 0
            if (cur_sum-k) in prefix_count:
                count += prefix_count[cur_sum - k]
            prefix_count[cur_sum] += 1
        return count
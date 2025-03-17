class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
        
        res = sorted(nums, key=lambda x: (freq[x], -x)) # sorting is done by lexographical first by freq if freq is same then by value 
        return res
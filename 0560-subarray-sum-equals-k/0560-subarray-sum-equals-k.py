class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefixSum = 0
        count = 0
        hashmap = defaultdict(int)
        hashmap[0] = 1  

        for num in nums:
            prefixSum += num
            if prefixSum - k in hashmap:
                count += hashmap[prefixSum - k]
            hashmap[prefixSum] += 1

        return count
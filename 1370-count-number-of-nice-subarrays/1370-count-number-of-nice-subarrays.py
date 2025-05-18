class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        #this problem is exact similar to binary subarray with sum
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        count = 0
        currSum = 0
        for num in nums:
            currSum += 1 if num%2!=0 else 0
            if (currSum - k) in prefix_count:
                count += prefix_count[currSum - k]
            prefix_count[currSum] += 1
        return count

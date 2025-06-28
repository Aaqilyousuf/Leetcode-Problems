class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # subSeq = []
        # n = len(nums)
        # for mask in range(1<<n):
        #     sub = []
        #     for i in range(n):
        #         if mask & (1<<i):
        #             sub.append(nums[i])
        #     if len(sub) == k:
        #         subSeq.append(sub)
        # res = []
        # maxSum = float('-inf')
        # for sub in subSeq:
        #     if sum(sub) > maxSum:
        #         maxSum = sum(sub)
        #         res = sub
        # return res

        numsWithI = [(num, i) for i, num in enumerate(nums)]
        
        # Sort by value descending
        numsWithI.sort(key=lambda x: -x[0])
        
        
        top_k = sorted(numsWithI[:k], key=lambda x: x[1])
        
       
        return [num for num, _ in top_k]
        




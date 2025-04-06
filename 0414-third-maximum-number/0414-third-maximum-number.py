class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        numSet = set(nums)
        mx = max(nums)
        if len(numSet)<3:
            return mx
        heap = []
        for num in numSet:
            
            heapq.heappush(heap, num)

            if len(heap) >3:
                heapq.heappop(heap)
    
        return heap[0]

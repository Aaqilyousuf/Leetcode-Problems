class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = defaultdict(int)
        for n in nums:
            freqMap[n] += 1
        minHeap = []
        for num, freq in freqMap.items():
            heapq.heappush(minHeap, (freq, num))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        res = []
        while minHeap:
            res.append(heapq.heappop(minHeap)[1])
        return res[::-1]
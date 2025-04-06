class Solution:
    def secondHighest(self, s: str) -> int:
        digits = set()
        for ch in s:
            if ch.isdigit():
                digits.add(int(ch))
        if len(digits) < 2:
            return -1
        heap = []
        for num in digits:
            heapq.heappush(heap, num)
            if len(heap) > 2:
                heapq.heappop(heap)
        return heap[0]

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        minHeap = []#to store the end time
        day = 0
        attended = 0
        i = 0
        n = len(events)
        while i < n or minHeap:
            if not minHeap:
                day = events[i][0]
            while i < n and events[i][0] <= day:
                heapq.heappush(minHeap, events[i][1])#endDay
                i += 1
            while minHeap and minHeap[0] < day:#3xpired events
                heapq.heappop(minHeap)
            if minHeap:#if not then attend and pop the end time
                heapq.heappop(minHeap)
                attended += 1
            day += 1
        return attended

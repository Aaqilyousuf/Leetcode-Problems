import heapq

class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        meetings.sort()                  #Sort meetings by start time
        free = list(range(n))            #Min-heap of available rooms by index
        heapq.heapify(free)

        busy = []                        #Min-heap of (endTime, room)
        count = [0] * n                  #Count of meetings per room

        for s, e in meetings:
            #Release rooms that are now free
            while busy and busy[0][0] <= s:
                _, r = heapq.heappop(busy)
                heapq.heappush(free, r)

            if free:
                r = heapq.heappop(free)
                new_end = e
            else:
                end_time, r = heapq.heappop(busy)
                new_end = end_time + (e - s)

            heapq.heappush(busy, (new_end, r))
            count[r] += 1
        max_index = 0
        for i in range(1, n):
            if count[i] > count[max_index]:
                max_index = i
        return max_index

        # return max(range(n), key=count.__getitem__)

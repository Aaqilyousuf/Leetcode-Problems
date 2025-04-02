class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)
        for u, v, w in times:
            adjList[u].append((v, w))
        heap = [(0, k)]
        minDist = {}
        while heap:
            time, node = heapq.heappop(heap)
            if node in minDist:
                continue
            minDist[node] = time
            for nei, weight in adjList[node]:
                if nei not in minDist:
                    heapq.heappush(heap, (time+weight, nei))
        return max(minDist.values()) if len(minDist) == n else -1
            


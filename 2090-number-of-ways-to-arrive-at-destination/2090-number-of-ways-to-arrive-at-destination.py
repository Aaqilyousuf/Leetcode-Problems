class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9+7
        adjList = defaultdict(list)
        for u, v, w in roads:
            adjList[u].append((v, w))
            adjList[v].append((u, w))
        heap = [(0, 0)] #time, src
        shortest = {i: float('inf') for i in range(n)}
        shortest[0] = 0
        pathCount = {i:0 for i in range(n)}
        pathCount[0] = 1

        while heap:
            time, node = heapq.heappop(heap)
            if time>shortest[node]:#outDated
                continue
            for nei, weight in adjList[node]:
                newTime = time+weight
                if newTime<shortest[nei]:
                    shortest[nei] = newTime
                    pathCount[nei] = pathCount[node] #reset
                    heapq.heappush(heap, (newTime, nei))
                    
                elif newTime == shortest[nei]:
                    pathCount[nei] = (pathCount[nei] + pathCount[node]) % MOD #add count
        return pathCount[n-1] % MOD
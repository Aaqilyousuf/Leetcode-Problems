class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adjList = defaultdict(list)
        for v1, v2, weight in edges:
            adjList[v1].append((v2, weight))
            adjList[v2].append((v1, weight))
        def dijkstras(src):
            heap = [(0, src)]
            visited = set()
            while heap:
                dist, node = heapq.heappop(heap)
                if node in visited:
                    continue
                visited.add(node)
                for nei, dist2 in adjList[node]:
                    nei_dist = dist + dist2
                    if nei_dist<=distanceThreshold:
                        heapq.heappush(heap, (nei_dist, nei))
            return len(visited)-1


        res, min_cost = -1, n
        for src in range(n):
            count = dijkstras(src)
            if count<=min_cost:
                min_cost = count
                res = src
        return res
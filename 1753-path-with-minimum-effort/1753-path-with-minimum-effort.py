class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        #djikstras algo
        rows, cols = len(heights), len(heights[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  

        minHeap = [(0, 0, 0)]
        distance = [[float('inf')] * cols for _ in range(rows)]
        distance[0][0] = 0

        while minHeap:
            r, c, e = heapq.heappop(minHeap)
            if r==rows-1 and c==cols-1:
                return e
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                
                if 0<=nr<rows and 0<=nc<cols:
                    newEffort = max(e , abs(heights[r][c] - heights[nr][nc]))
                    if newEffort < distance[nr][nc]:
                        distance[nr][nc] = newEffort
                        heappush(minHeap, (nr, nc, newEffort))
        return -1
        
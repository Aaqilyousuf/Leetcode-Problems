class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        queue = deque([(0,0,1)])
        visited = set()
        direction = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,-1],[-1,1],[1,-1]]
        while queue:
            r, c, dist = queue.popleft()
            if r==n-1 and c==n-1:
                return dist
            for dr, dc in direction:
                nr, nc = dr+r, dc+c
                if nr<0 or nc < 0 or nr>=n or nc>=n or grid[nr][nc] == 1 or (nr, nc) in visited:
                    continue
                visited.add((nr,nc))
                queue.append((nr, nc, dist+1))
        return -1


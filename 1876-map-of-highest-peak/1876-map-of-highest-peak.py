class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        ROWS, COLS = len(isWater), len(isWater[0])
        height = [[-1] * COLS for _ in range(ROWS)]
        queue = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if isWater[r][c] == 1:
                    queue.append((r,c))
                    height[r][c] = 0
        
        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                newR, newC = row+dr, col+dc
                if newR>=0 and newR<ROWS and newC>=0 and newC<COLS and height[newR][newC] == -1:
                    height[newR][newC] = height[row][col] + 1
                    queue.append((newR, newC))
        return height
        
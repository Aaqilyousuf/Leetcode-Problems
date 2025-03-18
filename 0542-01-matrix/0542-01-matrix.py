class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        queue = deque()
        ROWS, COLS = len(mat), len(mat[0])
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append((i, j, 0))
                else:
                    mat[i][j] = float("inf")
        while queue:
            row, col, dist = queue.popleft()
            if mat[row][col] > dist:
                mat[row][col] = dist
            for dr, dc in directions:
                nextR, nextC, nextVal = row+dr, col+dc, dist+1
                if nextR<0 or nextR>=ROWS or nextC<0 or nextC>=COLS:
                    continue
                if mat[nextR][nextC] == float("inf"):
                    queue.append((nextR, nextC, nextVal))
        return mat
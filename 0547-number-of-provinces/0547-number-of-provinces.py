class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        provinces = 0
        def dfs(node):
            for nighbour in range(n):
                if isConnected[node][nighbour] == 1 and nighbour not in visited:
                    visited.add(nighbour)
                    dfs(nighbour)

        for i in range(n):
            if i not in visited:
                provinces += 1
                visited.add(i)
                dfs(i)
        return provinces
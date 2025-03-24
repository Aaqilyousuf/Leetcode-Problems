class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def bfs(start):
            queue = deque([start])
        
            colors[start] = 0

            while queue:
                node = queue.popleft()
                for nei in graph[node]:
                    if nei in colors:
                        if colors[nei] == colors[node]:
                            return False
                    else:
                        queue.append(nei)
                        colors[nei] = 1 - colors[node]
            return True
        colors = {}
        for node in range(len(graph)):
            if node not in colors:
                if not bfs(node):
                    return False
        return True
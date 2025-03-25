class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        outDegree = [0] * n
        rev_adj = [[] for _ in range(n)]
        for u in range(n):
            for v in graph[u]:
                rev_adj[v].append(u)
            outDegree[u] = len(graph[u])
        queue = deque()

        for node in range(n):
            if outDegree[node] == 0:
                queue.append(node)
        safeNodes = []
        while queue:
            node = queue.pop()
            safeNodes.append(node)
            for nei in rev_adj[node]:
                outDegree[nei] -= 1
                if outDegree[nei] == 0:
                    queue.append(nei)
        return sorted(safeNodes)
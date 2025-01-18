class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        if not graph:
            return []
        target = len(graph) - 1
        t = len(graph) - 1
        stack = [(0, [0])]
        res = []
        while stack:
            node, path = stack.pop()
            if node == target:
                res.append(path)
            for n in graph[node]:
                stack.append((n, path+[n]))
        return res

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # graph_map = {}
        # for i, val in enumerate(graph):
        #     graph_map[i] = val
        target = len(graph) - 1
        res = []
        stack = [(0, [0])]

        while stack:
            node, path = stack.pop()

            if node == target:
                res.append(path)

            for neighbor in graph[node]:
                stack.append((neighbor, path+[neighbor]))
        return res
        
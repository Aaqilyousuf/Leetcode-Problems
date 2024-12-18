class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # this is DFS iterative approach, Three approached DFS(recursive), BFS
        edge_map = defaultdict(list)
        for start, end in edges:
            edge_map[start].append(end)
            edge_map[end].append(start)

        seen = set()
        seen.add(source)
        stack = [source]
        while stack:
            current = stack.pop()
            if current == destination:
                return True
            for neighbor in edge_map[current]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor) 

        return False
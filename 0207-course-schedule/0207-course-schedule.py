class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #topological sort method
        graph = defaultdict(list)
        for c, pre in prerequisites:
            graph[pre].append(c)
        visited = set()
        stack = []
        cycle = set()
        
        def dfs(node):
            if node in cycle:
                return False
            if node in visited:
                return True
            cycle.add(node)
            for neighbour in graph[node]:
                if not dfs(neighbour):
                    return False
            cycle.remove(node)
            visited.add(node)
            stack.append(node)
            return True


        for node in range(numCourses):
            if node not in visited:
                if not dfs(node):
                    return False
        return True
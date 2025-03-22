class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #topological sort method (khans algo
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        indegree = [0] * numCourses #num of edges connected to that current node
        for course, pre in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        count = 0
        while queue:
            node = queue.popleft()
            count += 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        return count == numCourses


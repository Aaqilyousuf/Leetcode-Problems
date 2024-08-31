from collections import defaultdict, deque
from typing import List

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        # Graph representation using adjacency list
        g, dq = defaultdict(list), deque([start])
        for i, (a, b) in enumerate(edges):
            g[a].append([b, i])
            g[b].append([a, i])

        # Probability array, initialized with 0 for all except the start node
        p = [0.0] * n    
        p[start] = 1.0

        # BFS to find the maximum probability path
        while dq:
            cur = dq.popleft()
            for neighbor, i in g[cur]:
                # If the probability of reaching neighbor via current node is higher, update it
                if p[cur] * succProb[i] > p[neighbor]:
                    p[neighbor] = p[cur] * succProb[i]
                    dq.append(neighbor)

        # Return the probability to reach the end node
        return p[end]

# To test the code
if __name__ == "__main__":
    # Example input
    n = 3
    edges = [[0,1],[1,2],[0,2]]
    succProb = [0.5,0.5,0.2]
    start = 0
    end = 2

    # Create an instance of Solution and call the method
    solution = Solution()
    result = solution.maxProbability(n, edges, succProb, start, end)
    print(f"The maximum probability of reaching node {end} from node {start} is: {result}")

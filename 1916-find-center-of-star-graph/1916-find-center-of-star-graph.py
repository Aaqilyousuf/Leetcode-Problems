class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        edge_list = {}
        for a, b in edges:
            if a not in edge_list:
                edge_list[a] = 0
            if b not in edge_list:
                edge_list[b] = 0
            edge_list[a] += 1
            edge_list[b] += 1

        for i, j in edge_list.items():
            if j == len(edges):
                return i
        return -1 
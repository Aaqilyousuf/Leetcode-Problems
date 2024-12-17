# class Solution:
#     def findCenter(self, edges: List[List[int]]) -> int:
#         edge_list = {}
#         for a, b in edges:
#             if a not in edge_list:
#                 edge_list[a] = 0
#             if b not in edge_list:
#                 edge_list[b] = 0
#             edge_list[a] += 1
#             edge_list[b] += 1

#         for i, j in edge_list.items():
#             if j == len(edges):
#                 return i
#         return -1 
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # The center node must be common in the first two edges
        if edges[0][0] in edges[1]:
            return edges[0][0]
        return edges[0][1]

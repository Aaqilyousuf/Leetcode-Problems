from collections import defaultdict
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points_direction = []
        for point in points:
            e = point[0]**2 + point[1]**2
            eq = math.sqrt(e)
            points_direction.append((eq, point))

        points_direction.sort(key=lambda x:x[0])
        
        return [point for _, point in points_direction[:k]]

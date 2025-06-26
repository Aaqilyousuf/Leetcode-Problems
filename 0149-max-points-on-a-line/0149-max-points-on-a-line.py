class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        if len(points) == 2:
            return len(points)
        mx = 0
        n = len(points)
        for i in range(n):
            slopes = defaultdict(int)
            samePoint = 1
            for j in range(i+1, n):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]

                if dx == 0 and dy == 0:
                    samePoint += 1
                    continue
                if dx == 0:
                    slope = (float('inf'), 0)
                elif dy == 0:
                    slope = (0, 0)
                else:
                    g = gcd(dx, dy)
                    dy//=g
                    dx//=g

                    if dx<0:
                        dy, dx = -dy, -dx
                    slope = (dy, dx)
                slopes[slope] += 1
            mx = max(mx, samePoint+max(slopes.values(), default=0))
        return mx

        
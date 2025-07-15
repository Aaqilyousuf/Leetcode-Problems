class Solution:
    def numSquares(self, n: int) -> int:
        ps = []
        i = 1
        while i*i <= n:
            ps.append(i*i)
            i += 1
        print(ps)
        #DP bottom up table
        # dp = [float('inf')] * (n+1)
        # dp[0] = 0
        # for p in ps:
        #     for i in range(p, n+1):
        #         dp[i] = min(dp[i], dp[i-p] + 1)
        # return dp[n] if dp[n] != float('inf') else -1
        #Using BFS
        queue = deque([(n, 0)]) #n, steps
        visited = set()
        while queue:
            rem, steps = queue.popleft()
            if rem == 0:
                return steps
            for sq in ps:
                newRem = rem-sq
                if newRem < 0:
                    break
                if newRem not in visited:
                    visited.add(newRem)
                    queue.append((newRem, steps+1))
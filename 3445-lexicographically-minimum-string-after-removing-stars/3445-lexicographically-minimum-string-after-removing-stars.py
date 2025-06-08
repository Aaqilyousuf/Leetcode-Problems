class Solution:
    def clearStars(self, s: str) -> str:
        charMap = defaultdict(list)
        pq = []
        keep = [True] * len(s)
        for i in range(len(s)):
            if s[i] == "*":
                small = heapq.heappop(pq)
                ind = charMap[small].pop()
                keep[i] = False
                keep[ind] = False

            else:
                heapq.heappush(pq, s[i])
                charMap[s[i]].append(i)
        return "".join(s[i] for i in range(len(s)) if keep[i])
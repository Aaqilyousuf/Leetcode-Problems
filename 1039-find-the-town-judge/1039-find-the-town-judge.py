class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n==1:
            return 1
        trust_list = [0] * (n+1)

        for a, b in trust:
            trust_list[a] -= 1
            trust_list[b] += 1

        for i in range(1, n+1):
            if trust_list[i] == n-1:
                return i
        return -1
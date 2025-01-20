class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        hashMap = defaultdict(list) #it could be normal dict (hashMap = {})

        for r in range(n):
            for c in range(m):
                hashMap[mat[r][c]] = [r, c]
        rowFreq = [0] * n
        colFreq = [0] * m
        for i in range(n*m):
            if arr[i] in hashMap:
                r, c = hashMap[arr[i]]
                rowFreq[r] += 1
                colFreq[c] += 1

                if rowFreq[r] == m or colFreq[c] == n:
                    return i
        return

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        def countNoSubSeq(sub, curStr):
            i, j = 0, 0
            count = 0
            n, m = len(curStr), len(sub)
            while i<n:
                while i<n and j<m and curStr[i] == sub[j]:
                    i+=1
                    j+=1
                    if j==m:
                        j = 0
                        count += 1
                i += 1
            return count
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        q = deque()
        curr = ""
        q.append(curr)
        res = ""

        while q:
            curr = q.popleft()
            nxt = curr
            for i in range(ord('a'), ord('z')+1, 1):
                if freq[i - ord('a')] < 2:
                    continue
                nxt += chr(i)
                if countNoSubSeq(nxt, s) >= k:
                    res = nxt
                    q.append(nxt)
                nxt = nxt[:-1]
        return res



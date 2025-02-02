class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        hashMap = defaultdict(int)
        resLen = float('inf')
        cnt = 0
        res = [-1, -1]
        for i in range(len(t)):
            hashMap[t[i]] += 1
        l = 0
        for r in range(len(s)):
            if hashMap[s[r]] > 0:
                cnt += 1
            hashMap[s[r]] -= 1
            while cnt == len(t):
                if r-l+1<resLen:
                    resLen = r-l+1
                    res = [l, r]
                hashMap[s[l]] += 1
                if hashMap[s[l]] > 0:
                    cnt -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float('inf') else ""
 

            
class Solution:
    def maxDepth(self, s: str) -> int:
        max_cnt = -1
        cnt = 0
        for c in s:
            if c=="(":
                cnt+=1
            elif c==")":
                cnt-=1
            max_cnt = max(max_cnt, cnt)
        return max_cnt
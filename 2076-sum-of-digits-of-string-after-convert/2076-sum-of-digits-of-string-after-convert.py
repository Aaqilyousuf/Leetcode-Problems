class Solution:
    def getLucky(self, s: str, k: int) -> int:
        res = ""
        ans = 0
        for i in s:
            val = ord(i) - ord('a') + 1
            res += str(val) 
        while k > 0:
            for j in res:
                ans = ans + int(j)
            res = str(ans)
            if k > 1:
                ans = 0
            k -= 1
        return ans

        
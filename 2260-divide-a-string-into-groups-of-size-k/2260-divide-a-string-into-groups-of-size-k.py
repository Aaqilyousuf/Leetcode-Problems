class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        l = len(s)
        res = []
        for i in range(0, l, k):
            res.append(s[i:i+k])
        rem = l%k
        if rem==0:
            return res
        add = k - rem
        last = res.pop()
        for i in range(add):
            last += fill
        res.append(last)
        return res

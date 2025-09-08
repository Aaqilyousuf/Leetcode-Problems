class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n):
            a = str(i)
            b = str(n-i)
            if '0' in a or '0' in b:
                continue
            return [int(a), int(b)]
        return [int(a), int(b)]
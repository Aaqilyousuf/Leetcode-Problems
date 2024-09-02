class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        tot = sum(chalk)
        k = k % tot
        i = 0
        for i, num in enumerate(chalk):
            if k < num:
                return i
            k = k - num
        
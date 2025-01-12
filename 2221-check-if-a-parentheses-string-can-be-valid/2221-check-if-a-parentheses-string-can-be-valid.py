class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if len(s) & 1:
            return False
        if len(s) != len(locked):
            return False
        wildCard, open, close = 0, 0, 0
        for i in range(len(s)):
            if locked[i] == "0": wildCard+=1
            elif s[i] == "(": open += 1
            else: close += 1

            if wildCard < (close - open):
                return False
        wildCard, open, close = 0, 0, 0
        for i in range(n-1, -1, -1):
            if locked[i] == "0": wildCard += 1
            elif s[i] == "(": open += 1
            else: close += 1

            if wildCard < (open - close):
                return False
        return True

        
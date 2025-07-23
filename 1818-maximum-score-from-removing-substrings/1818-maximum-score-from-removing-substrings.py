class Solution:
    def computeScore(self, s, pair, score):
        stack = []
        total_score = 0
        for c in s:
            if stack and stack[-1] == pair[0] and c == pair[1]:
                stack.pop()
                total_score += score
            else:
                stack.append(c)
        return ("".join(stack), total_score)
    def maximumGain(self, s: str, x: int, y: int) -> int:
        maxi = 0
        if x>y:
            firstpair = "ab"
            fs = x
            secondpair = "ba"
            ss = y
        else:
            firstpair = "ba"
            fs = y
            secondpair = "ab"
            ss = x
        s, score1 = self.computeScore(s, firstpair, fs)
        s, score2 = self.computeScore(s, secondpair, ss)
        return score1 + score2

        
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(open, close, subset):
            if len(subset) == 2*n:
                res.append(subset)
                return
            if open<n:
                backtrack(open+1, close, subset+'(')
            if close<open:
                backtrack(open, close+1, subset+')')

        res = []
        backtrack(0,0, "")
        return res
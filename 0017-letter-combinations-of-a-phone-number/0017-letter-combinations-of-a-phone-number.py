class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        phoneMap = {
            '2':"abc",
            '3':"def",
            '4':"ghi",
            '5':"jkl",
            '6':"mno",
            '7':"pqrs",
            '8':"tuv",
            '9':"wxyz"
        }
        combo = []
        for s in digits:
            combo.append(phoneMap[s])
        res = []
        def dfs(start, path):
            if start == len(combo):
                res.append("".join(path))
                return
            for ch in combo[start]:
                path.append(ch)
                dfs(start+1, path)
                path.pop()
        dfs(0, [])
        return res
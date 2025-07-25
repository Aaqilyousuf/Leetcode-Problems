class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # colMap = {}
        # for i in range(1, 27):
        #     colMap[chr(64+i)] = i
        # print(colMap)
        # res = 0
        # i = len(columnTitle)-1
        # for t in columnTitle:
        #     res += colMap[t] * (26**i)
        #     i -= 1
        # return res
        res = 0
        for char in columnTitle:
            res = res * 26 + (ord(char) - ord('A') + 1)
        return res


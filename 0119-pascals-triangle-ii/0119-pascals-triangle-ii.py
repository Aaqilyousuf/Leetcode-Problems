class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = []
        for i in range(1, rowIndex+2):
            ans.append(self.genRows(i))
        res = ans[rowIndex]
        return res
    def genRows(self, row):
        ansRow = []
        val = 1
        ansRow.append(val)
        for col in range(1, row):
            val = val * (row-col)
            val = val//col
            ansRow.append(val)
        return ansRow

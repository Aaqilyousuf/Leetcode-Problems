class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(1, numRows+1):
            ans.append(self.genRows(i))
        return ans
    def genRows(self, row):
        initVal = 1
        ansRow = []
        ansRow.append(initVal)
        for col in range(1, row):
            initVal = initVal * (row-col)
            initVal = initVal//col
            ansRow.append(initVal)
        return ansRow
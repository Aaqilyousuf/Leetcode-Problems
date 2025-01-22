class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        row, col = len(matrix), len(matrix[0])
        prefixSum = [[0]*col for _ in range(row)]
        maxArea = 0
        for j in range(col):
            sum = 0
            for i in range(row):
                sum += int(matrix[i][j])
                if matrix[i][j] == '0':
                    sum = 0
                prefixSum[i][j] = sum
        for i in range(row):
            area = self.histogram(prefixSum[i])
            maxArea = max(maxArea, area)
        return maxArea
    def histogram(self, row):
        stack = []
        n = len(row)
        maxArea = 0
        for i in range(n):
            while stack and row[stack[-1]] > row[i]:
                ind = stack.pop()
                nse = i
                pse = -1 if not stack else stack[-1]
                area = row[ind] * (nse-pse-1)
                maxArea = max(maxArea, area)
            stack.append(i) #index
        while stack:
            ind = stack.pop()
            nse = n
            pse = -1 if not stack else stack[-1]
            area = row[ind] * (nse-pse-1)
            maxArea = max(maxArea, area)
        return maxArea
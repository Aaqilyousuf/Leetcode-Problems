class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix) #rows
        m = len(matrix[0]) #cols
        low, high = 0, m*n - 1
        while low <= high:
            mid = low + (high - low)//2
            row = mid // m #current row
            col = mid % m #current col
            if matrix[row][col] == target:
                return True
            if matrix[row][col] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False
        # rows, cols = len(matrix), len(matrix[0])
        # for i in range(rows):
        #     for j in range(cols):
        #         if matrix[i][j] == target:
        #             return True
        # return False
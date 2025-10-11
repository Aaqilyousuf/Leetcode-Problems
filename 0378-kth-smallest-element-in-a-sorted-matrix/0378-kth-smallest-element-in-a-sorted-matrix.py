class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        l, h = matrix[0][0], matrix[-1][-1]

        while l<h:
            mid = (l+h)//2
            count = 0
            col = n-1
            for row in range(n):
                while col>=0 and matrix[row][col] > mid:
                    col -= 1
                count += (col+1)
            if count<k:
                l = mid + 1
            else:
                h = mid

        return l
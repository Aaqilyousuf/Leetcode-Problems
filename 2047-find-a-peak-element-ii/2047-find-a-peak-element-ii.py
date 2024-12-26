class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        n = len(mat) #rows
        m = len(mat[0]) #cols
        low, high = 0, m - 1
        while low<=high:
            mid = (low+high) // 2
            maxInd = self.findMax(mat, n, m, mid)
            left = mat[maxInd][mid-1] if mid > 0 else -1
            right = mat[maxInd][mid+1] if mid < m-1 else -1
            if left < mat[maxInd][mid] and mat[maxInd][mid] > right:
                return [maxInd, mid]
            if mat[maxInd][mid] < left:
                high = mid - 1
            else:
                low = mid + 1
        return [-1, -1] 

    def findMax(self, mat, n, m, mid):
        curmax = -1
        ind = -1
        for i in range(n):
            if mat[i][mid] > curmax:
                curmax = mat[i][mid]
                ind = i
        return ind
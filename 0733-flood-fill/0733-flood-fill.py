class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        original = image[sr][sc]
        def dfs(sr, sc):
            if image[sr][sc] != original or image[sr][sc] == color:
                return
            image[sr][sc] = color
            if sr+1<rows and image[sr+1][sc] == original:
                dfs(sr+1, sc)
            if sc+1<cols and image[sr][sc+1] == original:
                dfs(sr, sc+1)
            if sr>0 and image[sr-1][sc] == original:
                dfs(sr-1, sc)
            if sc>0 and image[sr][sc-1] == original:
                dfs(sr, sc-1)

        dfs(sr, sc)
        return image





    
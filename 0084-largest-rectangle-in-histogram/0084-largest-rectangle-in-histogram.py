class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # maxArea = 0
        # stack = []
        # for i, h in enumerate(heights):
        #     start = i
        #     while stack and stack[-1][1] > h:
        #         index, height = stack.pop()
        #         start = index
        #         maxArea = max(maxArea, height * (i-index))            
        #     stack.append((start, h))
        # for i, h in stack:
        #     maxArea = max(maxArea, h * (len(heights) - i))
        # return maxArea
        maxArea = 0
        n = len(heights)
        stack = [] #stores only the index
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                ind = stack.pop()
                nse = i #next smallest element
                pse = -1 if not stack else stack[-1] #previous smallest emelent
                area = heights[ind] * (nse-pse-1)
                maxArea = max(maxArea, area)
            stack.append(i)
        while stack:
            ind = stack.pop()
            nse = n
            pse = -1 if not stack else stack[-1]
            area = heights[ind] * (nse-pse-1)
            maxArea = max(maxArea, area)
        return maxArea


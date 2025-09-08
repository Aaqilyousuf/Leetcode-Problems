class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        ng = {}
        for n in nums2:
            while stack and stack[-1] < n:
                small = stack.pop()
                ng[small] = n
            stack.append(n)
        while stack:
            ng[stack.pop()] = -1
        ans = []
        for n in nums1:
            ans.append(ng[n])
        return ans 


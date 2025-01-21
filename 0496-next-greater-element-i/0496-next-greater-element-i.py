class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_great = {}
        for n in nums2:
            while stack and stack[-1] < n:
                smaller = stack.pop()
                next_great[smaller] = n
            stack.append(n)

        while stack:
            next_great[stack.pop()] = -1
        ans = []
        for num in nums1:
            ans.append(next_great[num])
        return ans


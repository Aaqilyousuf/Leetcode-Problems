class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1:
            if len(nums2) == 1:
                return nums2[0]
            elif len(nums2) % 2 == 0:
                m = len(nums2) // 2
                return (nums2[m] + nums2[m-1]) / 2
        if not nums2:
            if len(nums1) == 1:
                return nums1[0]
            elif len(nums1) % 2 == 0:
                m = len(nums1) // 2
                return (nums1[m] + nums1[m-1]) / 2

        merged = nums1 + nums2
        merged.sort()
        m = 0
        l = len(merged)
        if l % 2 == 0:
            m = l // 2
            return (merged[m] + merged[m-1]) / 2
        else:
            m = l // 2
            return merged[m]
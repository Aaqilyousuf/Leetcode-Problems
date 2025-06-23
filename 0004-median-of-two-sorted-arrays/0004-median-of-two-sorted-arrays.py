class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0, 0
        l1, l2 = len(nums1), len(nums2)
        res = []
        while i<l1 and j<l2:
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
        while i<len(nums1):
            res.append(nums1[i])
            i+=1
        while j<len(nums2):
            res.append(nums2[j])
            j += 1
        n = len(res)
        if n % 2 == 0:
            return (res[n//2] + res[(n//2) - 1]) / 2
        else:
            return res[n//2] 
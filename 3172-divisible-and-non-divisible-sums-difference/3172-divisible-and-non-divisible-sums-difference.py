class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        nums1, nums2 = [], []
        for num in range(1, n+1):
            if num % m != 0:
                nums1.append(num)
            else:
                nums2.append(num)
        return sum(nums1) - sum(nums2)
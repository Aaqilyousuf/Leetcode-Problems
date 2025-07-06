class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        oldVal = self.nums2[index]
        self.freq[oldVal] -= 1
        if self.freq[oldVal] == 0:
            del self.freq[oldVal]
        self.nums2[index] += val
        self.freq[self.nums2[index]] += 1
        

    def count(self, tot: int) -> int:
        tcnt = 0
        for a in self.nums1:
            tcnt += self.freq.get(tot-a, 0)
        return tcnt


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
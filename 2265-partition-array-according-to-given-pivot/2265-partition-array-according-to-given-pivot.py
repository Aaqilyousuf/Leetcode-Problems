

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lessThan = [x for x in nums if x < pivot]
        equal = [x for x in nums if x == pivot]
        greater = [x for x in nums if x > pivot]

        return lessThan + equal + greater

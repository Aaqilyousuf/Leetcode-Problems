class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i, val in enumerate(nums):
            difference = target - val
            if difference in map:
                return [map[difference], i]
            map[val] = i
        return []
            
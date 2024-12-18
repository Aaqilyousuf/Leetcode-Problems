class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map = {}
        for i, n in enumerate(numbers):
            comp = target - n
            if comp in map:
                return [map[comp]+1, i+1]
            map[n] = i
        return -1
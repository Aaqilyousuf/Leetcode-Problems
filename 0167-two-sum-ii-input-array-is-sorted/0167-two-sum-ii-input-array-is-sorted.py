class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # map = {}
        # for i, n in enumerate(numbers):
        #     comp = target - n
        #     if comp in map:
        #         return [map[comp]+1, i+1]
        #     map[n] = i
        # return -1
        l, r = 0, len(numbers) - 1
        while l < r:
            cur = numbers[l] + numbers[r]
            if cur > target:
                r -= 1
            elif cur < target:
                l += 1
            else:
                return [l+1, r+1]
        return []
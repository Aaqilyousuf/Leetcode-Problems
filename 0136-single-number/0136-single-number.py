class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        map = {}
        for n in nums:
            if n in map:
                map[n] += 1 
            else:
                map[n] = 1
        for n in map:
            if map[n] == 1:
                return n
            
             
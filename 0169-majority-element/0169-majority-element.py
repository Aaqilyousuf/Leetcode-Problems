class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #O(1) space
        res = majority = 0
        
        for n in nums:
            if majority == 0:
                res = n
            
            majority += 1 if n == res else -1
        
        return res
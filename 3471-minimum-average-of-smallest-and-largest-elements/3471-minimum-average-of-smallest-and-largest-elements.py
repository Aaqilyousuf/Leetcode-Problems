class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        avg = []
    
        while nums:
            large = max(nums)
            small = min(nums)
            a = (small+large)/2
            avg.append(a)
            if large == small:
                nums.remove(large)
            else:
                nums.remove(large) 
                nums.remove(small) 

        return min(avg)
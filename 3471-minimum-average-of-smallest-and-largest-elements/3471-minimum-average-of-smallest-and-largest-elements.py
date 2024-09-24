class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        # avg = []
    
        # while nums:
        #     large = max(nums)
        #     small = min(nums)
        #     a = (small+large)/2
        #     avg.append(a)
        #     if large == small:
        #         nums.remove(large)
        #     else:
        #         nums.remove(large) 
        #         nums.remove(small) 

        # return min(avg)
        nums.sort()
        avg = []
        n = len(nums)
        for i in range(n//2):
            minEl = nums[i]
            maxEl = nums[n-1-i]
            a = (minEl+maxEl)/2
            avg.append(a)
        return min(avg)
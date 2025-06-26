from math import gcd
class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        max_num = max(nums)
        
        pres = [False] * (max_num +1)
        for num in nums:
            pres[num] = True
        count =0


        for d in range(1, max_num + 1):
            g =0 
         
            for j in range(d, max_num+1, d):
                if pres[j]:
                    g= gcd(g,j)
                    #if alread here
                    if g==d:
                        count += 1
                        break
        return count
 


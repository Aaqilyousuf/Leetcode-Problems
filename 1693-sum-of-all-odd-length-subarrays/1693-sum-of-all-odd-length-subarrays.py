class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        #in this problem we find no of sub array 
        res = 0
        n = len(arr)
        for i in range(len(arr)):
            end = i + 1
            start = n-i
            total = start * end 
            odd = total//2
            if total%2==1: #if the total is even then i would not comes under odd subarray sum
                odd += 1 #why odd+=1 is because if tot=9 then if we divide then it would be 4 but 9 is odd so we add 1 to make it odd
            res += odd*arr[i] #number if times X current number
        return res
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
    
        for i in range(0, floor(sqrt(c))+1):
            sum = c - i**2
            if sum >= 0 and sqrt(sum) == int(sqrt(sum)):  # Check if sum is a perfect square
                return True
        return False
        
        
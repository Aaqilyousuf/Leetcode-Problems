class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
       
        flips = 0
        while k > 1:
            if k % 2 == 0:  
                flips += 1
            else:           
                pass
            k = (k + 1) // 2  

        return flips % 2  

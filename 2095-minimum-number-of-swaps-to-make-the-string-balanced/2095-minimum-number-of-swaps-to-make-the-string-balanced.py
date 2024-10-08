class Solution:
    def minSwaps(self, s: str) -> int:
        balance = 0
        swap = 0
        for char in s:
            if char=="[":
                balance += 1
            else:
                balance -= 1

            if balance < 0:
                swap+=1
                balance += 2
        return swap

                
            
                
        
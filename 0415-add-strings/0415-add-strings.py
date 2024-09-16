class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        res = []
        
        while i >= 0 or j >= 0 or carry:
            total = carry  # Start with carry
            
            if i >= 0:
                total += int(num1[i])
                i -= 1
                
            if j >= 0:
                total += int(num2[j])
                j -= 1
            
            carry = total // 10
            res.append(str(total % 10))
        
        return ''.join(res[::-1])  # Reverse and join the result list into a string

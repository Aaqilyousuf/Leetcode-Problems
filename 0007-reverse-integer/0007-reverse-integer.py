class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        is_neg = x < 0
        x = abs(x)
        while x > 0 :
            digit = x%10
            res = (res * 10) + digit
            x = x // 10
        if is_neg:
            res = -res
        if res < -2**31 or res > 2**31 - 1:
            return 0
        return res 
     
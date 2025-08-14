class Solution:
    def largestGoodInteger(self, num: str) -> str:
        checkSum = ['999', '888', '777', '666', '555', '444', '333', '222', '111', '000']
        for c in checkSum:
            if c in num:
                return c
        return ""
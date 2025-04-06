class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        # ls = list(number)
        # ind = -1
        # for i in range(len(ls)-1):
        #     if digit == ls[i]:
        #         if int(ls[i]) < int(ls[i+1]):
        #             del ls[i]
        #             return "".join(ls)
                    
        # ind = number.rfind(digit)
        # del ls[ind]
        # return "".join(ls)
        #optimal
        for i in range(len(number) - 1):
            if number[i] == digit and number[i] < number[i + 1]:
                return number[:i] + number[i + 1:]
        
        idx = number.rfind(digit)
        return number[:idx] + number[idx + 1:]

        
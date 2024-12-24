class Solution:
    def largestOddNumber(self, num: str) -> str:
        # l = len(num) - 1
        # if num[l] == "0":
        #     if int(num[:l]) % 2 != 0:
        #         return num[:l]

        # if int(num) % 2 != 0:
        #     return num
        # odd = ""
        # for n in num:
        #     if int(n) % 2 != 0:
        #         odd += n
        #     else:
        #         continue
        # return odd
        l = len(num)-1
        for r in range(l, -1, -1):
            if int(num[r]) %2 != 0:
                return num[:r+1]
        return ""

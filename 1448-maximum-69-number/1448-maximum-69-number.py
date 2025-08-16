class Solution:
    def maximum69Number (self, num: int) -> int:
        maxVal = -1
        sn = list(str(num))
        print(sn)
        for i in range(len(sn)):
            if sn[i] == "6":
                sn[i] = "9"
                break
        return int("".join(sn))

            

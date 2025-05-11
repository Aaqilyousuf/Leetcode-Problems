class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        oddCnt = 0
        for n in arr:
            if n&1==1:
                oddCnt += 1
                if oddCnt == 3:
                    return True
            else:
                oddCnt = 0
        return False
            
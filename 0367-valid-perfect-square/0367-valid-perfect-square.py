class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # if num==1:
        #     return True
        # i = 1
        # for i in range(1, num):
        #     if i*i == num:
        #         return True
        # return False 
        left, right = 1, num
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                left = mid + 1
            else:
                right = mid - 1
        return False
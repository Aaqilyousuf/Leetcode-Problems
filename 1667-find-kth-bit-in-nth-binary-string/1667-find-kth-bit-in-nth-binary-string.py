class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def helper(n, k):
            if n == 1:
                return "0"
            mid = 2 ** (n - 1)
            if k == mid:
                return "1"
            elif k < mid:
                return helper(n - 1, k)
            else:
                mirror = 2 ** n - k
                bit = helper(n - 1, mirror)
                return "0" if bit == "1" else "1" #inverting the op

        return helper(n, k)

#Because:

#The right half is a mirror image of the left half — flipped and reversed.

#So when you want to find a value in the right half, you:

#Mirror the index: find where that bit originally came from in Sn-1

#Invert the value (because it was inverted during construction)
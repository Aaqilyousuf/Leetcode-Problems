class Solution(object):
    def isPalindrome(self, x):
       n=x
       res=0
       while(n>0):
        l=n%10
        res=(res*10)+l
        n=n/10
       if res==x:
        return True
       
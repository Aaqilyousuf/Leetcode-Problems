class Solution:
    def numberOfMatches(self, n: int) -> int:
        number_of_matches = 0
        while n!=1:
            if n%2==0:
                number_of_matches+=n//2
                n=n//2
            else:
                number_of_matches+=(n-1)//2
                n=((n-1)//2)+1
        return number_of_matches

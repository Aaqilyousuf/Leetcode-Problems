class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = list(range(1,n+1))
        ci = 0
        while len(friends) > 1:
            ci = (ci + k - 1)%len(friends)
            friends.pop(ci)
        return friends[0]

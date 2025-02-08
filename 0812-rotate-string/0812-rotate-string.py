class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        if s==goal:
            return True
        res = s + s
        return goal in res

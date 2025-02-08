class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        stot = {}
        ttos = {}
        for c1, c2 in zip(s, t):
            if c1 in stot and stot[c1] != c2:
                return False
            if c2 in ttos and ttos[c2] != c1:
                return False
            stot[c1] = c2
            ttos[c2] = c1
        return True
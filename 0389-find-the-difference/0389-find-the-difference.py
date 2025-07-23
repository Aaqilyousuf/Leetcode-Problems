from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sl, tl = len(s), len(t)
        smap = Counter(s)
        tmap = Counter(t)
        for i in t:
            if i not in smap:
                return i
            elif tmap[i] > smap[i]:
                return i
            else:
                continue
        return ""
        
            
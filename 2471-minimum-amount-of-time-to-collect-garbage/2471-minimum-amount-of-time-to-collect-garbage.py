class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        totalGarbage = 0
        for g in garbage:
            totalGarbage += len(g)
        lastM, lastP, lastG = -1, -1, -1
        for i in range(len(garbage)):
            if 'M' in garbage[i]:
                lastM = i
            if 'P' in garbage[i]:
                lastP = i
            if 'G' in garbage[i]:
                lastG = i
        prefix = [0] * len(garbage)
        for i in range(1, len(garbage)):
            prefix[i] = prefix[i-1] + travel[i-1]
        ans = totalGarbage
        if lastM!=-1:
            ans += prefix[lastM]
        if lastP!=-1:
            ans += prefix[lastP]
        if lastG!=-1:
            ans += prefix[lastG]
        return ans
        

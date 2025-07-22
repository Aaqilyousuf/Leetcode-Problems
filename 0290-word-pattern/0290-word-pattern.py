class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        #n2
        # ls = s.split()
        # patternInd = []
        # for p in pattern:
        #     patternInd.append(pattern.index(p))
        # sind = []
        # for word in ls:
        #     sind.append(ls.index(word))
        
        # return patternInd == sind

        ls = s.split()
        if len(ls) != len(pattern):
            return False
        ptos = {}
        stop = {}
        for p, w in zip(pattern, ls):
            if p in ptos:
                if ptos[p] != w:
                    return False
            else:
                ptos[p] = w
            
            if w in stop:
                if stop[w] != p:
                    return False
            else:
                stop[w] = p
        return True
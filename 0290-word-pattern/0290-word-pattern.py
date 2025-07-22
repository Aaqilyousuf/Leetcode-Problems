class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ls = s.split()
        patternInd = []
        for p in pattern:
            patternInd.append(pattern.index(p))
        sind = []
        for word in ls:
            sind.append(ls.index(word))
        
        return patternInd == sind

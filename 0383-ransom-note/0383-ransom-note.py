class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False
        freqNote = defaultdict(int)
        freqMag = defaultdict(int)
        for c in ransomNote:
            freqNote[c] += 1
        for c in magazine:
            freqMag[c] += 1
        for c in ransomNote:
            if c in magazine and freqMag[c] >= freqNote[c]:
                continue
            else:
                return False
        return True
            
        
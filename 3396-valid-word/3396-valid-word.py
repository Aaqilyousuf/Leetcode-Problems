class Solution:
    def isValid(self, word: str) -> bool:
        n = len(word)
        if n < 3:
            return False
        vowel = "aeiouAEIOU"
        v = 0
        c = 0
        if word.isalnum():
            for ch in word:
                if ch in vowel:
                    v += 1
                elif ch.isdigit():
                    continue
                else:
                    c += 1
        if v >= 1 and c >= 1:
            return True
        return False
        
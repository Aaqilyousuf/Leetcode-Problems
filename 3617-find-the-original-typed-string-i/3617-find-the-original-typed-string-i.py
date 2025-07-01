class Solution:
    def possibleStringCount(self, word: str) -> int:
        count = 1
        for i in range(1, len(word)):
            if word[i] == word[i-1]:
                count += 1
        
        if count - 1 == len(word):
            return count-1
        return count
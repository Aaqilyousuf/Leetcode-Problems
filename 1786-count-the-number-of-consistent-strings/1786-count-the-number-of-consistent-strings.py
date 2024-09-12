class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        
        for word in words:
            for w in word:
                if w in allowed:
                    pass
                else:
                    break
            else:
                count += 1

                    
        return count
        
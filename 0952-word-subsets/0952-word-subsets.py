from collections import Counter
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        max_freq = Counter()
        for word in words2:
            word_freq = Counter(word)
            for char in word_freq:
                max_freq[char] = max(max_freq[char], word_freq[char])
        def isSubset(word_freq, max_freq):
            for char in max_freq:
                if word_freq[char] < max_freq[char]:
                    return False
            return True
        res = []
        for word in words1:
            word_freq = Counter(word)
            if isSubset(word_freq, max_freq):
                res.append(word)
        return res
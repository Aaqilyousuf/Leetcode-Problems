from collections import Counter
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        letters_count = Counter(letters)
        def get_merged_word(bitmask) -> str:
            merge_word = ""
            for i in range(len(words)):
                if not bitmask & 1<<i:
                    continue
                merge_word += words[i]
            return merge_word

        def is_valid_word(merge_word) -> bool:
            count_chars = Counter(list(merge_word))
            for char, count in count_chars.items():
                if count > letters_count[char]:
                    return False
            return True

        def get_score(merge_word) -> int:
            BASE = ord("a")
            word_score = 0
            for c in merge_word:
                word_score += score[ord(c) - BASE]
            return word_score

        res = 0
        for bitmask in range(1, 1<<len(words)):
            merge_word = get_merged_word(bitmask)
            if is_valid_word(merge_word):
                res = max(res, get_score(merge_word))
        return res
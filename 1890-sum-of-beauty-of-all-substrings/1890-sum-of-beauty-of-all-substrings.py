class Solution:
    def beautySum(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            alpha = [0] * 26  # Frequency array for characters 'a' to 'z'
            for j in range(i, len(s)):
                alpha[ord(s[j]) - ord('a')] += 1
                res += self.beauty(alpha)
        return res

    def beauty(self, alpha):
        max_freq = max(alpha)  # Maximum frequency of any character
        min_freq = float('inf')

        for freq in alpha:
            if freq >= 1:
                min_freq = min(min_freq, freq)

        return max_freq - min_freq

# from collections import defaultdict

# class Solution:
#     def plzhelp(self, s: str, k: int) -> int:
#         #This is done using a two-pointer sliding window approach combined with the "at most K distinct characters" trick
#         i = 0
#         count = 0
#         char_freq = defaultdict(int)

#         for j in range(len(s)):
#             char_freq[s[j]] += 1

#             while len(char_freq) > k:
#                 char_freq[s[i]] -= 1
#                 if char_freq[s[i]] == 0:
#                     del char_freq[s[i]]
#                 i += 1

#             count += (j - i + 1)

#         return count

#     def numberOfSubstrings(self, s: str) -> int:
#         k = 3
#         return self.plzhelp(s, k) - self.plzhelp(s, k - 1)
from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        i = 0
        count = 0
        char_freq = defaultdict(int)

        for j in range(n):
            char_freq[s[j]] += 1

            while char_freq['a'] >= 1 and char_freq['b'] >= 1 and char_freq['c'] >= 1:
                count += (n - j)

                # Shrinking the window
                char_freq[s[i]] -= 1
                i += 1

        return count

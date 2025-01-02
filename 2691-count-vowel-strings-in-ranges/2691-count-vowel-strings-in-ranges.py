class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        def ifVowel(ch: str) -> bool:
            vowels = {'a', 'e', 'i', 'o', 'u'}
            return ch in vowels

        n = len(words)
        prefix = [0] * n
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        # Build the prefix sum array
        for i in range(n):
            startCh = words[i][0]
            endCh = words[i][-1]
            if ifVowel(startCh) and ifVowel(endCh):
                prefix[i] = 1
        for i in range(1, n):
            prefix[i] += prefix[i - 1]

        ans = []
        for l, r in queries:
            left_sum = prefix[l - 1] if l > 0 else 0
            right_sum = prefix[r]
            ans.append(right_sum - left_sum)

        return ans

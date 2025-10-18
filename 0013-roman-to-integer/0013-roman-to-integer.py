class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
        }
        total = 0
        i = 0
        while i<len(s):
            curVal = roman_to_int[s[i]]
            if i+1<len(s):
                nextVal = roman_to_int[s[i+1]]
                if nextVal > curVal:
                    total += (nextVal - curVal)
                    i += 2 #skip the next val also
                    continue
            total += curVal
            i += 1
        return total
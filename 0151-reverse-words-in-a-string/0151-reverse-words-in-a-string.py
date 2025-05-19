class Solution:
    def reverseWords(self, s: str) -> str:
        st = s.split()
        l, r = 0, len(st) - 1
        while l<=r:
            st[l], st[r] = st[r], st[l]
            l += 1
            r -= 1

        return " ".join(st)
class Solution:
    def reverseWords(self, s: str) -> str:
        st = []
        i = 0 
        n = len(s)
        while i<n:
            while i<n and s[i] == " ":
                i+=1
            if i>=n:
                break
            j = i
            while j<n and s[j] != " ":
                j+=1
            st.append(s[i:j])
            i = j

        l, r = 0, len(st) - 1
        while l<=r:
            st[l], st[r] = st[r], st[l]
            l += 1
            r -= 1

        return " ".join(st)
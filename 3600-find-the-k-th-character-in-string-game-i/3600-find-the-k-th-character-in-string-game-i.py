class Solution:
    def kthCharacter(self, k: int) -> str:
        q = ["ab"]
        i = 0
        while True:
            word = q[i]
            ch = ""
            for w in word:
                ch += chr(((ord(w) - ord('a') + 1) % 26) + ord('a'))
            q.append(ch)
            if len(q) !=0 and len(q) & (len(q) - 1) == 0:
                i = 0
            elif i<len(q):
                i += 1
            if len(q)//2 >= k:
                break
        actualWord = "".join(q)
        print(actualWord)
        res = actualWord[k-1]
        return res
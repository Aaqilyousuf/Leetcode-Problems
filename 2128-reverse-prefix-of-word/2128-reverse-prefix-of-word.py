class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = 0
        if ch in word:
            index = word.index(ch)
        l=0
        r=index
        li = list(word)
        while l<=r:
            li[l], li[r]=li[r], li[l]
            l+=1
            r-=1
        res = "".join(li)
        return res
        
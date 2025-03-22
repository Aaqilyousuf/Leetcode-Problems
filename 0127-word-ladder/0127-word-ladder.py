class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = deque([(beginWord, 1)])
        st = set(wordList)
        while queue:
            word, cnt = queue.popleft()
            if word == endWord:
                return cnt
            wList = list(word)
            for i in range(len(word)):
                original = word[i]
                for ch in range(ord('a'), ord('z')+1):
                    wList[i] = chr(ch)
                    newWord = "".join(wList)
                    if newWord in st:
                        st.remove(newWord)
                        queue.append((newWord, cnt+1))
                wList[i] = original
        return 0

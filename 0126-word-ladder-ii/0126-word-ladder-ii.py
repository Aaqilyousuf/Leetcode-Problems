class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        graph = defaultdict(set)
        level = {beginWord: 0}
        queue = deque([beginWord])
        found = False

        while queue and not found:
            next_level = {}
            for _ in range(len(queue)):
                word = queue.popleft()
                curLevel = level[word]
                wList = list(word)
                for i in range(len(word)):
                    original = wList[i]
                    for ch in range(ord('a'), ord('z')+1):
                        wList[i] = chr(ch)
                        newWord = "".join(wList)
                        if newWord in wordSet:
                            if newWord not in level:
                                level[newWord] = curLevel + 1
                                queue.append(newWord)
                            if level[newWord] == curLevel + 1:
                                graph[newWord].add(word)
                                next_level[newWord] = True
                            if newWord == endWord:
                                found = True
                    wList[i] = original
            wordSet -= set(next_level.keys())
        res = []
        def backtrack(path, word):
            if word == beginWord:
                res.append(path)
                return
            for prev in graph[word]:
                backtrack([prev] + path, prev)
        if found:
            backtrack([endWord], endWord)


        return res

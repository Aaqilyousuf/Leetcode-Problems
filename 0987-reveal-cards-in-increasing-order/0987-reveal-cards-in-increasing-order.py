class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n = len(deck)
        Queue = list(range(n))
        ans = [None] * n
        for card in deck:
            ans[Queue.pop(0)] = card
            if Queue:
                Queue.append(Queue.pop(0))
        return ans

        
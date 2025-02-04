class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        cardCount = defaultdict(int)
        for h in hand:
            cardCount[h] += 1
        minHeap = list(cardCount.keys())
        heapq.heapify(minHeap)

        while minHeap:
            firstCard = minHeap[0]
            for i in range(groupSize):
                curr = firstCard + i
                if cardCount[curr] == 0:
                    return False
                cardCount[curr] -= 1
                if cardCount[curr] == 0:
                    if minHeap[0] == curr:
                        heapq.heappop(minHeap)
        return True
        

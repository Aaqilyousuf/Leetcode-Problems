class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        maxCount = 0
        i, j = 0, 0
        players.sort()
        trainers.sort()
        print(trainers)
        pn, tn = len(players), len(trainers)

        while i<pn and j<tn:
            
            if players[i] <= trainers[j]:
              
                maxCount += 1
                i += 1
                # j += 1
            j += 1
        return maxCount

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        count = 0
        n = len(fruits)
        used = [False] * len(baskets)
        for i in range(n):
            for j in range(n):
                if fruits[i]<=baskets[j] and not used[j]:
                    used[j] = True
                    count += 1
                    break
        
        res = n-count
        return res
            
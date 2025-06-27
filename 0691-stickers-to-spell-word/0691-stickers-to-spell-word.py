class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        def dfs(memo, stickerCounters, target):
            if not target:
                return 0
            if target in memo:
                return memo[target]
            targetCounter = Counter(target)
            res = float('inf')
            for stickerCount in stickerCounters:
                if stickerCount[target[0]] == 0:
                    continue
                remchar = targetCounter - stickerCount
                temp = [k*v for k, v in remchar.items()]
                nextTarget = "".join(temp)
                res = min(res, 1 + dfs(memo, stickerCounters, nextTarget))
            memo[target] = res
            return res
        
        memo = {}
        stickerCounters = [Counter(sticker) for sticker in stickers]
        res = dfs(memo, stickerCounters, target)
        return res if res != float('inf') else -1
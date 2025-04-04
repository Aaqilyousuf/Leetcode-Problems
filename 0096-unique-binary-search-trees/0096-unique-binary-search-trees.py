class Solution:
    def numTrees(self, n: int) -> int:
        if n==1:
            return 1
        numTree = [1] * (n+1)

        for node in range(2, n+1):
            tot = 0
            for root in range(1, node+1):
                left = root-1
                right = node-root
                tot += numTree[left] * numTree[right]
            numTree[node] = tot
        return numTree[n]



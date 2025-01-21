# class Solution:
#     def sumSubarrayMins(self, arr: List[int]) -> int:
#         #brute force
#         sum = 0
#         MOD = int(1e9 + 7)
#         n = len(arr)
#         for i in range(n):
#             mini = arr[i]
#             for j in range(i, n):
#                 mini = min(mini, arr[j])
#                 sum = (sum + mini) % MOD
#         return sum
        #optimal
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = [] # keep index for the latest smaller values
        res = [0] * len(arr)

        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()

            j = stack[-1] if stack else -1
            res[i] = res[j] + (i - j) * arr[i]

            stack.append(i)
        
        return sum(res) % (10**9+7)
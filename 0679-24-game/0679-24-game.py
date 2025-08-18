class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        limit = 1e-9
        def calc(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24.0) <= limit
            
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i==j:
                        continue


                    nextData = []
                    for k in range(len(nums)):
                        if k!=i and k!=j:
                            nextData.append(nums[k])
                    operations = [
                        nums[i] + nums[j],
                        nums[i] - nums[j],
                        nums[j] - nums[i],
                        nums[i] * nums[j]
                    ]
                    if nums[i] != 0:
                        operations.append(nums[j] / nums[i])
                    if nums[j] != 0:
                        operations.append(nums[i] / nums[j])
                    for op in operations:
                        if calc(nextData + [op]):
                            return True
            return False
        

        return calc(cards)
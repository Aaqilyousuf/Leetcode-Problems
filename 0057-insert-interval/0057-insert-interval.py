class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key = lambda x: x[0])
        res = []
        current = intervals[0]
        for i in range(1, len(intervals)):
            if current[1] >= intervals[i][0]:
                current[1] = max(current[1], intervals[i][1])
            else:
                res.append(current)
                current = intervals[i]

        res.append(current)
        return res

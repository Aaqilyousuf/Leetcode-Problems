class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # count = defaultdict(int)
        # for task in tasks:
        #     count[task] += 1
        # maxHeap = [-x for x in count.values()]
        # heapq.heapify(maxHeap)

        # time = 0
        # q = deque() #pairs of [-cnt, ideleTime]

        # while maxHeap or q:
        #     time += 1
        #     if maxHeap:
        #         cnt = 1 + heapq.heappop(maxHeap)
        #         if cnt < 0:
        #             q.append([cnt, time+n])
        #     if q and q[0][1] == time:
        #         heapq.heappush(maxHeap, q.popleft()[0])
        # return time
        task_counts = Counter(tasks)
        
        
        max_freq = max(task_counts.values())
        
       
        max_freq_tasks = 0
        for count in task_counts.values():
            if count == max_freq:
                max_freq_tasks += 1

        return max(len(tasks), (max_freq - 1) * (n + 1) + max_freq_tasks)

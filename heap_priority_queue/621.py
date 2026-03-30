from collections import deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for task in tasks:
            count[task] = count.get(task, 0) + 1
        
        heap = [(count[task], task) for task in count]
        heapq.heapify_max(heap)

        q = deque()
        time = 0

        while heap or q:
            time += 1

            if heap:
                cnt, task = heapq.heappop_max(heap)
                cnt -= 1
                if cnt:
                    q.append([(cnt, task), time + n])

            if q and q[0][1] == time:
                heapq.heappush_max(heap, q.popleft()[0])

        return time

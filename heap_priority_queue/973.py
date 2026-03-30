import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = [((a ** 2 + b ** 2) ** (1/2), i)  for i,(a,b) in enumerate(points)]
        heapq.heapify(dist)
        res = []
        for _ in range(k):
            res.append(points[dist[0][1]])
            heapq.heappop(dist)
        return res
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums
        heapq.heapify_max(heap)
        for _ in range(k):
            max_seen = heapq.heappop_max(heap)
        return max_seen
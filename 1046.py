import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = stones
        heapq.heapify_max(stones) # max heap, heaviest at the top

        def lastStoneHeap(heap):
            if len(heap) == 0:
                return 0

            if len(heap) == 1:
                return heap[0]

            y = heap[0]
            x = heap[1]

            if x == y:
                heapq.heappop_max(heap)
                heapq.heappop_max(heap)

            if y != x:
                heapq.heappop_max(heap)
                heapq.heappop_max(heap)
                heapq.heappush_max(heap,y-x)

            return lastStoneHeap(heap)

        return lastStoneHeap(heap)
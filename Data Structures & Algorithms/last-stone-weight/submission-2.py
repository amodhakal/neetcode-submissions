import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        heapq.heapify(heap)

        for stone in stones:
            heapq.heappush(heap, -stone)

        while len(heap) > 1:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)
            if first == second:
                continue

            new_weight = first - second
            heapq.heappush(heap, new_weight)

        if len(heap) == 1:
            return -(heap[0])
        return 0

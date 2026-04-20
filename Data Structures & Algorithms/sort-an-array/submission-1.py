import heapq

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heap = []
        heapq.heapify(heap)

        for num in nums:
            heapq.heappush(heap, num)

        result = []
        while len(heap) > 0:
            item = heapq.heappop(heap)
            result.append(item)

        return result

        
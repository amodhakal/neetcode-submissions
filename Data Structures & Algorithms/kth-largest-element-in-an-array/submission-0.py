class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = list(map(lambda x: -x, nums))
        heapq.heapify(pq)

        for i in range(k - 1):
            heapq.heappop(pq)

        return - heapq.heappop(pq)

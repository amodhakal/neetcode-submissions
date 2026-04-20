import heapq

class KthLargest:
    kth: int
    list: List[int] = []

    def __init__(self, k: int, nums: List[int]):
        self.list = []
        self.kth = k
        heapq.heapify(self.list)
        for num in nums:
            heapq.heappush(self.list, -num)

    def add(self, val: int) -> int:
        heapq.heapify(self.list)
        heapq.heappush(self.list, -val)
        remaining = []
        
        for i in range(0, self.kth):
            popped = heapq.heappop(self.list)
            remaining.append(popped)

        returning = remaining[-1]

        for item in remaining:
            heapq.heappush(self.list, item)

        return -returning

        
        

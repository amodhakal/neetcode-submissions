import heapq

class KthLargest:
    kth: int
    list: List[int] = []

    def __init__(self, k: int, nums: List[int]):
        self.kth = k
        heapq.heapify(self.list)
        for num in nums:
            heapq.heappush(self.list, num)

    def add(self, val: int) -> int:
        heapq.heappush(self.list, val)
        remaining = []
        
        for i in range(0, val):
            remaining.append(heapq.heappop())

        returning = remaining[-1]

        for items in remaining:
            heapq.heappush(self.list, items)

        return returning

        
        

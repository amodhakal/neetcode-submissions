class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.nums = list(map(lambda x: -x, self.nums))
        heapq.heapify(self.nums)
        print(self.nums)


    def add(self, val: int) -> int:
        heapq.heappush(self.nums, -val)
        data = []

        for i in range(self.k - 1):
            data.append(heapq.heappop(self.nums))

        final = heapq.heappop(self.nums)
        data.append(final)
        self.nums += data
        heapq.heapify(self.nums)

        return -final



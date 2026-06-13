class MinStack:

    def __init__(self):
        self.heap = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        heapq.heappush(self.heap, val)

    def pop(self) -> None:
        value = self.stack.pop()
        self.heap.remove(value)
        heapq.heapify(self.heap)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.heap[0]
        

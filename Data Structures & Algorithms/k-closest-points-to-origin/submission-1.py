import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        heapq.heapify(distances)

        for [x, y] in points:
            distance = math.sqrt(x * x + y * y)
            heapq.heappush(distances, (-distance, x, y))

            if len(distances) > k:
                heapq.heappop(distances)
        
        returning = []
        for (dist, x, y) in distances:
            returning.append([ x, y])
        
        return returning
import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        heapq.heapify(distances)

        for [x, y] in points:
            distance = math.sqrt(x * x + y * y)
            heapq.heappush(distances, -distance)

            if len(distances) > k:
                heapq.heappop(distances)
        
        returning = []
        for distance in distances:
            actual = -distance
            print("A", actual)

            for [x, y] in points:
                current = math.sqrt(x * x + y * y)
                print("C", current)
                if current == actual:
                    returning.append([x, y])
                
                if len(returning) == k:
                    return returning
 

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points_list = []
        heapq.heapify(points_list)

        for point in points:
            distance = point[0] ** 2 + point[1] ** 2
            heapq.heappush(points_list, [ distance, point])

        result = []
        for i in range(k):
            val = heapq.heappop(points_list)
            point = val[1]
            result.append(point)

        return result
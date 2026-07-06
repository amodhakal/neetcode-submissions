class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        total = 0
        visited = set()
        pq = []

        # Add first point to queue
        heapq.heappush(pq, (0, (points[0][0], points[0][1])))

        # If item in queue and all points have not been visited
        while pq or len(visited) < len(points):
            # Continue if already visited
            cost, curr = heapq.heappop(pq)
            if curr in visited:
                continue

            # Now visited
            visited.add(curr)
            total += cost

            # Go through the rest of the values and add the cost to pq
            for point in points:
                if (point[0], point[1]) in visited:
                    continue

                add_cost = abs(point[0] - curr[0]) + abs(point[1] - curr[1])
                heapq.heappush(pq, (add_cost, (point[0], point[1])))

        return total
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}

        cache[len(cost) - 1] = cost[-1]
        cache[len(cost) - 2] = cost[-2]

        for idx in range(len(cost) - 3, -1, -1):
            current = cost[idx]
            cache[idx] = current + min(cache[idx + 1], cache[idx + 2])
            
        return min(cache[0], cache[1])

        # Start from back, storing the min cost to get to the top
        # Use the cache to skip over possible stops
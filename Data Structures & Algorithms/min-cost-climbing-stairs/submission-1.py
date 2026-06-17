class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for idx in range(len(cost) - 3, -1, -1):
            current = cost[idx]
            cost[idx] = current + min(cost[idx + 1], cost[idx + 2])
            
        return min(cost[0], cost[1])

        # Start from back, storing the min cost to get to the top
        # Use the cache to skip over possible stops
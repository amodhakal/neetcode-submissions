class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = list(map(lambda x: -x, stones))

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if first == second:
                continue

            heapq.heappush(stones, first - second)

        return 0 if len(stones) == 0 else -stones[0]

        
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = max(piles)
        for eat_rate in range(1, max_pile + 1):
            time_taken = 0

            for pile in piles:
                remaining_pile = pile
                while remaining_pile > 0:
                    remaining_pile -= eat_rate
                    time_taken += 1

            if time_taken <= h:
                return eat_rate

        return 0

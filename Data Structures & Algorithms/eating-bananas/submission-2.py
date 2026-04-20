class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = max(piles)
        min_eat_rate = max_pile

        l = 1
        r = max_pile

        while l <= r:
            eat_rate = (l + r ) // 2
            time_taken = 0

            for pile in piles:
                time_taken += math.ceil(pile / eat_rate)

            if time_taken <= h:
                min_eat_rate = min(eat_rate, min_eat_rate)
                # check lower
                r = eat_rate - 1
            else:
                # check higher
                l = eat_rate + 1

        return min_eat_rate

        # max_pile = max(piles)
        # for eat_rate in range(1, max_pile + 1):
        #     time_taken = 0

        #     for pile in piles:
        #         remaining_pile = pile
        #         while remaining_pile > 0:
        #             remaining_pile -= eat_rate
        #             time_taken += 1

        #     if time_taken <= h:
        #         return eat_rate

        # return 0

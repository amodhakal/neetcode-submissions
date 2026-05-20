# I have h hours to eat the banana
# I need a speed of k per hour to eat the banana for all piles
# I have to finish banana for one pile before continuing to the next
# one
# I have to find the lowest k per hour
# Can do binary search to reduce time

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lowest_speed = math.inf
        l, r = 1, max(piles) + 1
        while l <= r:
            current_hour = h
            speed = (l + r) // 2

            for pile in piles:
                current_hour -= pile // speed
                remainder = pile % speed
                if remainder != 0:
                    current_hour -= 1

            if current_hour < 0:
                # Not finished
                l = speed + 1
            else:
                # Finished
                r = speed - 1
                lowest_speed = min(lowest_speed, speed)
        
        return lowest_speed
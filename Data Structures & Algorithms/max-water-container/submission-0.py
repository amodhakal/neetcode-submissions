class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxstorage = 0
        l, r = 0, len(heights) - 1

        while l <= r:
            maxstoreable = min(heights[l], heights[r])

            maxstorage = max(maxstorage, maxstoreable * (r - l))

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxstorage
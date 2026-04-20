class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        top_range = len(nums)
        xored = 0

        for i in range(0, top_range + 1):
            xored = xored ^ i

        for num in nums:
            xored = xored ^ num

        return xored
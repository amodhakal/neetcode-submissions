class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = 0
        for num in nums:
            sum = sum ^ num

        for i in range(0, len(nums) + 1):
            sum = sum ^ i

        return sum
        
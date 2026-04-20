class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            count = 0

            for num in nums:
                if num == i:
                    count += 1

            if count > 1:
                return i
        
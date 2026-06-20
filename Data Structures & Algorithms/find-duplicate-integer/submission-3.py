class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = 0, 0

        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]

            print(fast, slow)

            if (fast == slow):
                return fast


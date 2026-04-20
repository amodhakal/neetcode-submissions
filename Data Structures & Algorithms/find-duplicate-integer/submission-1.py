class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]

            if slow == slow2:
                return slow


        # My Code
        # starting_number_fast = 0
        # starting_number_slow = 0

        # while True:
        #     prev_slow = starting_number_slow
        #     prev_fast = starting_number_fast

        #     starting_number_slow = nums[starting_number_slow]
        #     starting_number_fast = nums[starting_number_fast]
        #     starting_number_fast = nums[starting_number_fast]

        #     if starting_number_slow  == starting_number_fast:
        #         return prev_slow
 
        
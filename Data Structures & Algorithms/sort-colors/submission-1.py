class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, m, h = 0, 0, len(nums) - 1

        while m <= h:
            # while mid 0
            if nums[m] == 0:
                # Swap mid, low, increment both
                nums[m], nums[l] = nums[l], nums[m]
                l += 1
                m += 1
            # while mid 1
            elif nums[m] == 1:
                # Increment mid
                m += 1
            # while mid 2
            else:
                # Swap mid, hight, decrement hight
                nums[m], nums[h] = nums[h], nums[m]
                h -= 1
        
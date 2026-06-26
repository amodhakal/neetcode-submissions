class Solution:
    def specialArray(self, nums: List[int]) -> int:
        largest_num = max(nums)
        l, r = 0, largest_num + 1

        while l <= r:
            x = (l + r) // 2
            result = 0
            for num in nums:
                if num >= x:
                    result += 1
            
            if result == x:
                return x

            if result < x:
                r = x - 1
            
            if result > x:
                l = x + 1

        return -1
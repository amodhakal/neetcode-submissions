class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        founded = {nums[idx]: idx for idx in range(len(nums))}
        print(founded)
        for num in nums:
            required = target - num
            if required == num:
                continue

            if required not in nums:
                continue

            return [ founded[num], founded[required]]

        return [0, 0]

            
        
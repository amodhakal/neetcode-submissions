class Solution:
    def canJump(self, nums: List[int]) -> bool:
        canreach = [False for i in range(len(nums))]
        canreach[-1] = True

        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, i + nums[i] + 1):
                if canreach[j]:
                    canreach[i] = True
                    break
            
        print(canreach)
        return canreach[0]
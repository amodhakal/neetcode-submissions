class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            current = nums[i]
            for j in range(i + 1, len(nums)):
                possible = nums[j]

                # An increasing subsequence is found
                if possible > current:
                    memo[i] = max(memo[i], memo[j] + 1)

        return max(memo)




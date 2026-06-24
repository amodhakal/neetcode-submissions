class Solution:
    def jump(self, nums: List[int]) -> int:
        minjump = [ math.inf for num in nums]
        minjump[-1] = 0

        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, i + nums[i] + 1):
                minjump[i] = min(minjump[i], minjump[j] + 1)

        print(minjump)
        return minjump[0]
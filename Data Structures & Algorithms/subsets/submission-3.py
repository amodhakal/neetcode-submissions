class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for num in nums:
            stored = []
            for item in result:
                stored.append(item + [num])

            result += stored

        return result
        
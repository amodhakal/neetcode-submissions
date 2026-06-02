class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = strs[0]

        for i in range(1, len(strs)):
            curr = strs[i]
            prefix = ""

            for i in range(0, len(curr)):
                if len(common_prefix) > i and curr[i] == common_prefix[i]:
                    prefix += curr[i]
                else:
                    common_prefix = prefix

            return common_prefix

            

        
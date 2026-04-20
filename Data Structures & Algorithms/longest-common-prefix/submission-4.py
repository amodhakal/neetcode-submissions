class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = strs[0]

        for i in range(1, len(strs)):
            curr = strs[i]
            prefix = ""

            for j in range(min(len(curr), len(common_prefix))):
                if curr[j] == common_prefix[j]:
                    prefix += curr[j]
                else:
                    break
                
            common_prefix = prefix

        return common_prefix

            

        
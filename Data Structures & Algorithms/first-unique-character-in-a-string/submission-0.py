class Solution:
    def firstUniqChar(self, s: str) -> int:
        values = dict(collections.Counter(s))

        for i in range(len(s)):
            ch = s[i]
            if values[ch] == 1:
                return i

        return -1
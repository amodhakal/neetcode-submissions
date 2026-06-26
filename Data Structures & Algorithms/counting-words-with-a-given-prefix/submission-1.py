class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        result = 0
        for word in words:
            val = word[:len(pref)]
            print(val)
            if val == pref:
                result += 1

        return result
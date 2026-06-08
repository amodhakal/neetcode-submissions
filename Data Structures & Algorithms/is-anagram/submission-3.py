class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countMap = dict()

        for ch in s:
            if ch not in countMap:
                countMap[ch] = 1
                continue

            countMap[ch] += 1

        for ch in t:
            if ch not in countMap:
                return False

            countMap[ch] -= 1
            if countMap[ch] == 0:
                del countMap[ch]
        
        return len(countMap) == 0

        
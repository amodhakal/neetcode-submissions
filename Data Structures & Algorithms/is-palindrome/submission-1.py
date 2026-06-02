class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        l = 0
        r = len(s) - 1
        while l <= r:
            start = s[l]
            if start < 'a' or start > 'z':
                l += 1
                continue
            
            end = s[r]
            if end < 'a' or end > 'z':
                r -= 1
                continue 

            print(start, end)

            if start != end:
                return False
            
            l += 1
            r -= 1

        return True

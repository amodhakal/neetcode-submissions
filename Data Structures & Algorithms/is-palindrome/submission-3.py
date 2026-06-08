class Solution:
    def isPalindrome(self, s: str) -> bool:
        changed = list(filter(lambda x: x.isalnum(), list(s.lower())))
        l, r = 0, len(changed) - 1

        while l <= r:
            if changed[l] != changed[r]:
                return False

            l += 1
            r -= 1

        return True    
        
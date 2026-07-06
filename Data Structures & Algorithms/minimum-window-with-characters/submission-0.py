class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        l, r = 0, 0

        first_found = set(t)
        # Expand until all of the items are found
        while first_found and r < len(s):
            curr_ch = s[r]
            res += curr_ch
            if curr_ch in first_found:
                first_found.remove(curr_ch)
            
            if first_found:
                r += 1

        if first_found or res == "":
            return ""

        print(l, r, res)
        return res

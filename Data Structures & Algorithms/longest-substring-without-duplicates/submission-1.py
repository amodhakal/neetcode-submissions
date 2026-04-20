class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        l = 0
        charset = set()

        for r in range(len(s)):  
            curr_ch = s[r]

            # Check if not available
            if curr_ch not in charset:
                charset.add(curr_ch)
                length = max(length, len(charset))
                continue

            # keep removing values from set until the duplicate is found
            while True:
                del_ch = s[l]

                # Move 1 ahead
                l += 1
                
                # if found
                if del_ch == curr_ch:
                    break
                else:
                    # if not found
                    charset.remove(del_ch)

        return length
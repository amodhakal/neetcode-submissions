class Solution:
    def isValid(self, s: str) -> bool:
        opening = []

        for ch in s:
            if ch in ["(", "{", "["]:
                opening.append(ch)
                continue

            closings = { ")": "(", "}": "{", "]": "["}

            if len(opening) == 0:
                return False

            value = opening.pop()
            closing = closings[ch]
            if value != closing:
                return False
            


        return len(opening) == 0
        
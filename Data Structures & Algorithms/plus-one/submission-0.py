class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        returning_val = []
        has_overflow = False
        digits[len(digits) -1] += 1
        for i in range(len(digits) -1, -1, -1):
            new_digit = digits[i]
            if has_overflow:
                new_digit += 1
                has_overflow = False

            if new_digit > 9:
                new_digit -= 10
                has_overflow = True
            
            returning_val.insert(0, new_digit)

        if has_overflow:
            returning_val.insert(0, 1)

        return returning_val
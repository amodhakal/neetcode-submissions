class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for charac in s:
            if charac == '(':
                stack.append("(")
                continue
            if charac == '{':
                stack.append("{")
                continue
            if charac == '[':
                stack.append("[")
                continue

            if charac == ')':
                item = stack.pop()
                if item != '(':
                    return False
            if charac == '}':
                item = stack.pop()
                if item != '{':
                    return False
            if charac == ']':
                item = stack.pop()
                if item != '[':
                    return False

        return len(stack) == 0
        
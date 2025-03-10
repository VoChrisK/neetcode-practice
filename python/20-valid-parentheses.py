class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char == '{' or char == '[' or char == '(':
                stack.append(char)
            elif (
                (char == ']' and len(stack) > 0 and stack[-1] == '[') 
                or (char == '}' and len(stack) > 0 and stack[-1] == '{') 
                or (char == ')' and len(stack) > 0 and stack[-1] == '(')
            ):
                stack.pop()
            else:
                return False

        return len(stack) == 0        

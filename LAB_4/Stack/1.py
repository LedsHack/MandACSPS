def isValid(s: str) -> bool:
    stack = []
    matching_brackets = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in matching_brackets.values():
            stack.append(char)
        elif char in matching_brackets:
            if stack and stack[-1] == matching_brackets[char]:
                stack.pop()
            else:
                return False
    return not stack
print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))

def decodeString(s: str) -> str:
    stack = []
    current_str = ""
    current_num = 0
    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == "[":
            stack.append((current_str, current_num))
            current_str, current_num = "", 0
        elif char == "]":
            prev_str, num = stack.pop()
            current_str = prev_str + num * current_str
        else:
            current_str += char
    return current_str
print(decodeString("3[a]2[bc]"))
print(decodeString("3[a2[c]]"))
print(decodeString("2[abc]3[cd]ef"))

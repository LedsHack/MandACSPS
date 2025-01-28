def reverse_string_recursive(s):
    if len(s) == 0:
        return
    print(s[-1], end="")
    reverse_string_recursive(s[:-1])
input_string = "tiger"
reverse_string_recursive(input_string)
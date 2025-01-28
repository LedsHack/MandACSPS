def climb_stairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

print(climb_stairs(2))
print(climb_stairs(3))
print(climb_stairs(4))
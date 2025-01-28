def my_pow(x, n):
    if n == 0:
        return 1
    if n < 0:
        x = 1 / x
        n = -n
    if n % 2 == 0:
        half = my_pow(x, n // 2)
        return half * half
    else:
        return x * my_pow(x, n - 1)

print(my_pow(2.00000, 10))
print(my_pow(2.10000, 3))
print(my_pow(2.00000, -2))
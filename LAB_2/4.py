def duplicate_zeros(arr):
    i = 0
    while i < len(arr):
        if arr[i] == 0:
            arr.insert(i + 1, 0)
            arr.pop()
            i += 1
        i += 1

mas1 = [1, 0, 2, 3, 0, 4, 5, 0]
duplicate_zeros(mas1)
print(mas1)
mas2 = [1, 2, 3]
duplicate_zeros(mas2)
print(mas2)


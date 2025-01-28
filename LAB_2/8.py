def validMountainArray(arr):
    if len(arr) < 3:
        return False
    i = 0
    while i + 1 < len(arr) and arr[i] < arr[i + 1]:
        i += 1
    if i == 0 or i == len(arr) - 1:
        return False
    while i + 1 < len(arr) and arr[i] > arr[i + 1]:
        i += 1
    return i == len(arr) - 1

arr1 = [2, 1]
print(validMountainArray(arr1))

arr2 = [3, 5, 5]
print(validMountainArray(arr2))

arr3 = [0, 3, 2, 1]
print(validMountainArray(arr3))

def replaceElements(arr):
    max_right = -1
    for i in range(len(arr) - 1, -1, -1):
        new_max = max(arr[i], max_right)
        arr[i] = max_right
        max_right = new_max
    return arr

arr1 = [17, 18, 5, 4, 6, 1]
print(replaceElements(arr1))

arr2 = [400]
print(replaceElements(arr2))

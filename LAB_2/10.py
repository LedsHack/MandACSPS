def sortArrayByParity(nums):
    even = [num for num in nums if num % 2 == 0]
    odd = [num for num in nums if num % 2 != 0]
    return even + odd

nums1 = [3, 1, 2, 4]
print(sortArrayByParity(nums1))
nums2 = [0]
print(sortArrayByParity(nums2))

def sorted_squares(nums):
    return sorted(num ** 2 for num in nums)
print(sorted_squares([-4,-1,0,3,10]))
print(sorted_squares([-7,-3,2,3,11]))
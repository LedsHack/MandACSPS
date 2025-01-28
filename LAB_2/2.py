def find_numbers_with_even_digits(nums):
    return sum(1 for num in nums if len(str(num)) % 2 == 0)
print(find_numbers_with_even_digits([12,245,2,6,7896]))
print(find_numbers_with_even_digits([555,901,482,1771]))
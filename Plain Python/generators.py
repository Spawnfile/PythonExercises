"""
def squeare_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result

"""
import sys

# Turning this function to a Generator
# generators DO NOT hold the whole output in memory, but yield one restul at the time
def squeare_numbers(nums):
    for i in nums:
        yield (i*i)

# my_nums = squeare_numbers([1,2,3,4,5])
my_nums = (x*x for x in [1,2,3,4,5]) # It's a generator that created with list comprehension

# print(sys.getsizeof(my_nums)) # returning the size ( byte ) of variable that wanted to be measure
# 88 byte as generator, 128 byte as list

print(my_nums)

for num in my_nums:
    print(num)



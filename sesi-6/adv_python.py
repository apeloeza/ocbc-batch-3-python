#Iterator
def square(nums):
    for num in nums:
        yield (num * num)

# nums = [1, 2, 3, 4, 5]
nums = [1, 2, 3, 4, 5].__iter__()

print(square(nums))

print(next(square(nums)))
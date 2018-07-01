nums = [10, 20, 30, 40, 50]

del nums[0]
print(nums)

del nums[0:3]
print(nums)

nums = [10, 20, 30, 40, 50]

del nums[len(nums) - 1]
print(nums)

del nums[-1]
del nums[-2]
print(nums)

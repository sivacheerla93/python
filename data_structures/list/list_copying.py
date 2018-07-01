nums = [10, 20, 30, 40, 50]

nums2 = nums[:]  # Here we're copying, not referring
print(nums2)

# If we add number to nums, nums2 can't be affected
nums.append(60)
print(nums)
print(nums2)

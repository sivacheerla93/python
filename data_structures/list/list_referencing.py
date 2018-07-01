nums = [10, 20, 30, 40, 50]

nums2 = nums
print(nums, nums2)  # both can refer same list

nums.append(60)  # if add number to nums, nums2 could be affected
print(nums2)

nums2.append(70)  # if add number to nums, nums2 could be affected
print(nums)

arr1 = [10, 20, 30]
arr2 = [10, 20, 30]

if arr1 == arr2:  # Compares data!
    print("Elements are same! ")
else:
    print("Elements aren't same!")

if arr1 is arr2:  # Compares memory locations
    print("Memory locations are same!")
else:
    print("Memory locations aren't same!")

print("Memory locations of arr1 & arr2 are respectively: ")
print(id(arr1))
print(id(arr2))

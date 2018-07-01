print("Enter numbers to get sum & average, enter 0 to stop: ")

total = 0
count = 0
num = 1

while num != 0:
    num = int(input())
    total += num
    count += 1
count -= 1  # decrement 1 as we enter 0 to stop
print("Entered numbers: ", count)
print("Sum of numbers: ", total)
print("Average of numbers: ", total // count)

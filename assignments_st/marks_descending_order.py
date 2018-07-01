marks = []
num = 0
print("Enter your marks to get them in descending order, -1 to stop: ")

while num != -1:
    num = int(input())
    marks.append(num)

marks.pop()
print("Entered marks: ", marks)

marks.sort()
print("Marks in ascending order: ", marks)

marks.reverse()
print("Marks in descending order: ", marks)

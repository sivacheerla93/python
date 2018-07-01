numList = [1, 2, 3, 4, 5]
strList = ['One', 'Two', 'Three', 'Four', 'Five']

# zipping
zipped = zip(numList, strList)
print(list(zipped))

# un-zipping
numList2, strList2 = zip(*zip(numList, strList))
print(list(numList2), list(strList2))

print(numList == list(numList2))
print(strList == list(strList2))

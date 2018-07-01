i = 1
while i <= 15:
    print(i, end=' ')  # where end = ' ', to print on same line
    i += 1
    if i > 16:
        break
else:
    print()
    print("If break is executed, else is bypassed")
    print("If break isn't executed, else is executed")

def even_numbers(start, end):
    start = start if start % 2 == 0 else start + 1
    for i in range(start, end + 1, 2):
        yield i


for i in even_numbers(1, 13):
    print(i)

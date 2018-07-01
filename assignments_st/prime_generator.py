def getPrimes(n):
    i = 2
    while i < n:
        prime = True
        for a in range(2, i):
            if i % a == 0:
                prime = False
                break
        if prime == True:
            yield i
        i += 1


for i in getPrimes(100):
    print(i)

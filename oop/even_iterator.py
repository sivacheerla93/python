class EvenIterator:
    def __init__(self, start, end):
        self.start = start if start % 2 == 0 else start + 1
        self.end = end

    def __iter__(self):
        self.value = self.start
        return self

    def __next__(self):
        if self.value <= self.end:
            v = self.value
            self.value += 2
            return v
        else:
            raise StopIteration


# use Iterator
en = EvenIterator(10, 30)
for n in en:
    print(n)

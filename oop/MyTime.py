class MyTime:
    def __init__(self, h=0, m=0, s=0):
        self.H = h
        self.M = m
        self.S = s

    @property  # Getter
    def total_seconds(self):
        return self.H * 60 * 60 + self.M * 60 + self.S

    def __str__(self):
        return "%02d:%02d:%02d" % (self.H, self.M, self.S)

    def __gt__(self, other):
        return self.total_seconds > other.total_seconds

    def __eq__(self, other):
        return self.total_seconds == other.total_seconds

    def __iadd__(self, other):
        if not isinstance(other, int):
            return self

        self.S += other
        if self.S > 59:
            self.S = self.S % 60
            self.M += 1
            if self.M > 59:
                self.M = 0
                self.H += 1

        return self


t1 = MyTime(10, 20, 30)
print(t1)
t2 = MyTime(1, 2, 3)
print(t1 > t2)
t2 += 60
print(t2)
t1 += "abc"
print(t1)

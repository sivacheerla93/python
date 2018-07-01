from threading import Thread


class PrimeThread(Thread):
    def __init__(self, num):
        super().__init__()
        self.num = num

    def run(self):
        for i in range(2, self.num // 2 + 1):
            if self.num % i == 0:
                print(self.num, "isn't prime bcz it is divisible by", i)
                break
            else:
                print(self.num, "is prime number!")


nums = [2, 3, 5, 7, 10, 12, 35, 678]

for n in nums:
    t = PrimeThread(n)
    t.start()

class my_numbers():
    def __init__(self, numbers: list):
        self.numbers = numbers

    def __iter__(self):
        self.index = 0
        self.a = self.numbers[self.index]
        return self

    def __next__(self):
        if self.index < len(self.numbers) - 1:
            x = self.a
            self.index += 1
            self.a = self.numbers[self.index]
            return x
        elif self.index == len(self.numbers) - 1:
            x = self.a
            self.index += 1
            return x
        else:
            raise StopIteration


my_class = my_numbers([1, 2, 3, 4, 5, 6, 7])
my_iter = iter(my_class)

for x in my_iter:
    print(x)
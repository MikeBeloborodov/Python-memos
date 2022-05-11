class my_list(list):
    def __getitem__(self, index):
        if index == 0:
            raise IndexError("Index out of range")
        if index > 0:
            return super().__getitem__(index - 1)
        if index < 0:
            return super().__getitem__(index)
    

def list_power_of_two(num_of_elems: int) -> list[int]:
    return my_list(2 ** i for i in range(1, num_of_elems + 1))

result = list_power_of_two(10)

print(result[1])

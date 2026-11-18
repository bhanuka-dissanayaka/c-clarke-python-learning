def num_generators():
    yield 10
    yield 22
    yield 30
    yield 22

def generate_numbers(num):
    for i in range(num):
        yield i

even_num_list = [i for i in range(10) if i%2 == 0]
even_num_gen = [i for i in range(10) if i%2 == 0]


print("Even number list", even_num_list)
print("Even Number generator", even_num_gen)

gen = num_generators()
print(next(num_generators()))
print(next(num_generators()))
print(next(num_generators()))



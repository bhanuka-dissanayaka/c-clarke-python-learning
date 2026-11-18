def num_generators():
    yield 10
    yield 22
    yield 30
    yield 22

gen = num_generators()
print(next(num_generators()))
print(next(num_generators()))
print(next(num_generators()))
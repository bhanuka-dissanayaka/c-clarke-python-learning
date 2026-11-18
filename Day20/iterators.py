from typing import List

student_names: List[str] = ["amal", "nimal", "kamal" , "sunimal"]
student_iterators = student_names.__iter__()

print(student_iterators)

try:
    print(student_iterators.__next__())
    print(student_iterators.__next__())
    print(student_iterators.__next__())
    print(student_iterators.__next__())
    print(student_iterators.__next__())
except StopIteration as e:
    print(e)

student_iterators = iter(student_names)
print(next(student_iterators))
print(next(student_iterators))

# class CountDown:
#     def __init__(self, num: int):
#         self.num = num
#     def __iter__(self):
#         return  self
#     def __next__(self):
#         if self.num == 0:
#             raise StopIteration
#         self.num -= 1
#         return self.num
#
# for i in CountDown(10):
#     print(i)

class NumberGenerator:
    def __init__(self, num: int):
        self.current = -1
        self.end_num = num
    def __iter__(self):
        return self
    def __next__(self):
        if self.current == self.end_num:
            raise StopIteration
        self.current += 1
        return self.current

for i in NumberGenerator(180):
    print(i)

print(hasattr(list, "__iter__"))  # True
print(hasattr(student_iterators, "__next__"))  # True




# class Iterator:
#     def __init__(self, start, stop):
#         self.start = start
#         self.stop = stop
#
#     def __iter__(self):
#         self.cur = self.start
#         return self
#
#     def __next__(self):
#         if self.cur <= self.stop:
#             self.cur += 1
#             return self.cur - 1
#         else:
#             raise StopIteration


# def example():
#     custom_obj = Iterator(1, 11)
#     obj_iter = iter(custom_obj)  # a = [1, 2, 3, 4] ->> # b = iter(a)
#     print(obj_iter)
#     for num in obj_iter:  # c = next(b) it gives us 1
#         print(num)  # c = next(b) it gives us 2
#         # c = next(b) it gives us 3
#         # c = next(b) it gives us 4
#
# example()


class SquareIterator:
    def __init__(self, x, stop):
        self.x = x
        self.stop = stop

    def __iter__(self):
        self.current = self.x
        return self

    def __next__(self):
        if self.current <= self.stop:
            self.current += 1
            return (self.current - 1) ** 2

        else:
            raise StopIteration


def my_square_nums():
    my_obj = SquareIterator(2, 10)
    my_iter = iter(my_obj)
    print(my_iter)
    for n in my_iter:
        print(n)

my_square_nums()
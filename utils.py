from functools import reduce
from itertools import tee
from collections import Counter


def get_data(filename):
    for line in open(filename, "r"):
        yield line.strip()


def per_char(iterable):
    for line in iterable:
        for char in line:
            yield char


def to_int(iterable):
    for x in iterable:
        yield int(x)


def split(char):
    def _split(iterable):
        for x in iterable:
            yield x.split(char)

    return _split


def take(take_num):
    def __take(iterable):
        take_list = []
        for x in iterable:
            take_list = [x] + take_list
            take_list = take_list[0:take_num]
            if len(take_list) == take_num:
                yield take_list

    return __take


def group_while(predicate):
    def __group_while(iterable):
        take_list = []
        for x in iterable:
            take_list = [x] + take_list if predicate(x) else take_list
            if not predicate(x) and len(take_list) > 0:
                yield take_list
                take_list = []

    return __group_while


def iter_filter(predicate):
    def __iter_filter(iterable):
        for x in iterable:
            if predicate(x):
                yield x

    return __iter_filter


def iter_count(iterable):
    first_it, second_it = tee(iterable)
    return sum(1 for _ in second_it), first_it


def compose(*functions):
    def __compose(initial_value):
        return reduce(
            lambda result, value: value(result), functions[::-1], initial_value
        )

    return __compose


def clamp(number, lower, upper):
    return max(lower, min(number, upper))


def bin_to_decimal(binary):
    number = 0
    for b in binary:
        number = (2 * number) + int(b)
    return number


def peak_reduce(func):
    def _peak(result, value):
        print(value)
        return func(result, value)

    return _peak


def peak_compose(func):
    def __peak_compose(value):
        func(value)
        return value

    return __peak_compose


def get_diff_with_dups(list_one, list_two):
    return list((Counter(list_one) - Counter(list_two)).elements())


def list_remove_by_index(m, index):
    return m[:index] + m[index + 1 :]

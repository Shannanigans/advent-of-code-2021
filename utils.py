from functools import reduce


def get_data(filename):
    for line in open(filename, "r"):
        yield line.strip()


def compose(*functions):
    def __compose(initial_value):
        return reduce(
            lambda result, value: value(result), functions[::-1], initial_value
        )

    return __compose


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

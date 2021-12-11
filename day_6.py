from utils import (
    get_data,
    per_char,
    compose,
    peak_compose,
    to_int,
    iter_filter,
)
from collections import Counter
from functools import reduce, lru_cache


def to_counter(iterable):
    yield Counter(iterable)


def get_counter_total(counter):
    return sum(counter.values())


@lru_cache(maxsize=None)
def get_new_index(total_index):
    is_spawn = total_index == 0
    new_index = 6 if is_spawn else total_index - 1
    return is_spawn, new_index


def new_counter_builder(old_counter, new_counter, old_index):
    is_spawn, new_index = get_new_index(old_index)
    new_counter = new_counter + Counter({new_index: old_counter[old_index]})
    new_counter = (
        new_counter + Counter({8: old_counter[old_index]}) if is_spawn else new_counter
    )
    return new_counter


def process_generation(counter):
    return reduce(
        lambda result, value: new_counter_builder(counter, result, value),
        counter,
        Counter(),
    )


def process(generations):
    def __process(iterable):
        return reduce(
            lambda result, _: process_generation(result),
            range(generations),
            next(iterable),
        )

    return __process


def main():
    compose(
        peak_compose(lambda x: print("Answer: ", x)),
        get_counter_total,
        process(256),  #  359999, 1631647919273
        # process(80),  #  5934, 359999
        to_counter,
        to_int,
        iter_filter(lambda x: x != ","),
        per_char,
        get_data,
    )("day_6_data.txt"),


if __name__ == "__main__":
    main()

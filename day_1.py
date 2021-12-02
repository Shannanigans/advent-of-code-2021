from functools import reduce
from utils import get_data, compose, take, to_int


is_increase = lambda current, previous: previous is not None and current > previous


def process_part_one(slide_num, file_path):
    return reduce(
        lambda result, values: result + 1
        if is_increase(values[0], values[1])
        else result,
        compose(take(slide_num), to_int, get_data)(file_path),
        0,
    )


print("part 1 test", process_part_one(2, "day_1_test_data.txt"))
print("part 1", process_part_one(2, "day_1_data.txt"))


# PART 2


def is_sum_increase(slide_num, values):
    previous_sum = sum(values[0 : slide_num - 1])
    current_sum = sum(values[1:slide_num])
    return is_increase(previous_sum, current_sum)


def process_part_two(slide_num, file_path):
    return reduce(
        lambda result, values: result + 1
        if is_sum_increase(slide_num, values)
        else result,
        compose(take(slide_num), to_int, get_data)(file_path),
        0,
    )


print("part 2 test", process_part_two(4, "day_1_test_data.txt"))
print("part 2", process_part_two(4, "day_1_data.txt"))

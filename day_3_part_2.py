from functools import reduce
from utils import get_data, bin_to_decimal, iter_count
from day_3_part_1 import count_ones, get_initial_state
from itertools import tee


def least(bit_position, counts):
    return 1 if counts["bin"][bit_position] < (counts["total_count"] / 2) else 0


def most(bit_position, counts):
    return 1 if counts["bin"][bit_position] >= (counts["total_count"] / 2) else 0


modes = {"least": least, "most": most}


def filter_by_digit(iterator, digit, bit_position):
    return filter(lambda x: int(x[bit_position]) == digit, iterator)


def find_digit(iterator, mode, bit_position):
    counts = reduce(count_ones, iterator, get_initial_state())
    digit = modes[mode](bit_position, counts)
    return digit


def found(count):
    return count == 1


def dig(iterator, mode, bit_position=0):
    first_it, second_it = tee(iterator)
    digit = find_digit(first_it, mode, bit_position)
    count, sub_set = iter_count(filter_by_digit(second_it, digit, bit_position))
    return next(sub_set) if found(count) else dig(sub_set, mode, bit_position + 1)


def answer(filename):
    return bin_to_decimal(dig(get_data(filename), "most")) * bin_to_decimal(
        dig(get_data(filename), "least")
    )


def main():
    # print("oxygen generator rating:", dig(get_data("day_3_test_data.txt"), "most"))
    # print("CO2 scrubber rating:", dig(get_data("day_3_test_data.txt"), "least"))
    # print(answer("day_3_test_data.txt"))
    print(answer("day_3_data.txt"))


if __name__ == "__main__":
    main()

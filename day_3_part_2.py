from functools import reduce
from utils import get_data, bin_to_decimal
from day_3_part_1 import count_ones, get_initial_state
from itertools import tee


def least(bit_position, counts):
    return 1 if counts["bin"][bit_position] < (counts["total_count"] / 2) else 0


def most(bit_position, counts):
    return 1 if counts["bin"][bit_position] >= (counts["total_count"] / 2) else 0


modes = {"least": least, "most": most}


def dig(iterator, mode, bit_position=0):
    first_it, second_it = tee(iterator)
    counts = reduce(count_ones, first_it, get_initial_state())
    digit = modes[mode](bit_position, counts)
    sub_set = list(filter(lambda x: int(x[bit_position]) == digit, second_it))
    return (
        sub_set[0] if len(sub_set) == 1 else dig(iter(sub_set), mode, bit_position + 1)
    )


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

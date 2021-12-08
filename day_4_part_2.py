from utils import get_data
from day_4_part_1 import (
    get_index_results,
    get_board_iter,
    get_super_set_call_values,
    answer,
)


def process(iterable, value_index=0, super_values=None, winning_boards=[]):
    result = get_index_results(iterable, value_index + 1, super_values)
    winning_boards = winning_boards + result["winners"]

    if len(result["remaining"]) == 0:
        return winning_boards

    return process(
        iter(result["remaining"]), value_index + 1, super_values, winning_boards
    )


def main():
    iterable = get_data("day_4_data.txt")
    super_values = get_super_set_call_values(iterable)
    winning_boards = process(
        iterable=get_board_iter(iterable), value_index=0, super_values=super_values
    )
    final_win = winning_boards[-1]
    winning_board, check_set = final_win
    print(
        "Part 2: ",
        answer(winning_board, check_set),
    )


if __name__ == "__main__":
    main()

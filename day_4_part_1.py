from utils import get_data, group_while, get_diff_with_dups
from itertools import tee
from functools import reduce


def get_row(row_string):
    return reduce(
        lambda result, value: result + [value] if value else result,
        row_string.split(" "),
        [],
    )


def get_board_string_iter(iterable):
    return group_while(lambda x: len(x) > 0)(iterable)


def get_board_iter(iterable):
    for board in get_board_string_iter(iterable):
        yield list(map(get_row, board))


def check_rows(board, check_set):
    return any(list(map(lambda x: len(get_diff_with_dups(x, check_set)) == 0, board)))


def get_col(board, col_index):
    return reduce(
        lambda result, value: result + [value[col_index]],
        board,
        [],
    )


def get_cols(board):
    num_of_cols = len(board[0])
    return reduce(
        lambda result, value: result + [get_col(board, value)],
        range(0, num_of_cols),
        [],
    )


def check_cols(board, check_set):
    return check_rows(get_cols(board), check_set)


def win_splitter(check_set):
    def __win_splitter(result, value):
        if any([check_rows(value, check_set), check_cols(value, check_set)]):
            result["winners"] = result["winners"] + [(value, check_set)]
        else:
            result["remaining"] = result["remaining"] + [value]
        return result

    return __win_splitter


def get_index_results(iterable, value_index, super_values):
    return reduce(
        win_splitter(super_values[0:value_index]),
        iterable,
        {"winners": [], "remaining": []},
    )


def get_first_winner(result):
    return result["winners"][0] if len(result["winners"]) > 0 else (False, False)


def failure_to_find(value_index, super_values):
    return value_index == len(super_values)


def found(board, check_set):
    return board and check_set


def process(iterable, value_index=0, super_values=None):
    first_it, second_it = tee(iterable)
    result = get_index_results(first_it, value_index + 1, super_values)
    board, check_set = get_first_winner(result)

    if found(board, check_set):
        return board, check_set

    return (
        "no winners"
        if failure_to_find(value_index, super_values)
        else process(second_it, value_index + 1, super_values)
    )


def get_final_num(check_set):
    return int(check_set[-1])


def get_flat_board(board):
    return [item for sublist in board for item in sublist]


def answer(board, check_set):
    return sum(
        map(int, get_diff_with_dups(get_flat_board(board), check_set))
    ) * get_final_num(check_set)


def get_super_set_call_values(iterable):
    return next(iterable).split(",")


def main():
    iterable = get_data("day_4_data.txt")
    super_values = get_super_set_call_values(iterable)
    board, check_set = process(
        iterable=get_board_iter(iterable), value_index=0, super_values=super_values
    )
    print("Part 1: ", answer(board, check_set))


if __name__ == "__main__":
    main()

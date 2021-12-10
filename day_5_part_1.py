from utils import get_data, split, compose, clamp
from functools import reduce

x_co = 0
y_co = 1


def get_coordinate_pairs(coordinate_pair):
    return coordinate_pair[x_co], coordinate_pair[y_co]


def is_perpendicular(coordinate_pair, check_index):
    first, second = get_coordinate_pairs(coordinate_pair)
    return first[check_index] == second[check_index]


def get_horizontal_vertical_iter(iterable):
    return filter(
        lambda coordinate_pair: is_perpendicular(coordinate_pair, x_co)
        or is_perpendicular(coordinate_pair, y_co),
        iterable,
    )


def list_to_int(x):
    return list(map(int, x))


def get_coordinates_iter(iterable):
    for x in split(" -> ")(iterable):
        yield (list_to_int(x[0].split(",")), list_to_int(x[1].split(",")))


def get_initial_map(x_limit, y_limit):
    return list(map(lambda _: list(map(lambda _: ".", range(x_limit))), range(y_limit)))


def map_mark_handler(value):
    return 1 if value == "." else clamp(value + 1, 0, 5)


def is_reversed(value1, value2):
    return value1 > value2


def rrange(value1, value2):
    return range(
        value1,
        value2 - 1 if is_reversed(value1, value2) else value2 + 1,
        -1 if is_reversed(value1, value2) else 1,
    )


def get_index_range(coordinate_pair, index_co):
    first, second = get_coordinate_pairs(coordinate_pair)
    range_coordinate = rrange(first[index_co], second[index_co])
    return range_coordinate


def is_diagonal(coordinate_pair):
    # assumes if not perpendicular then diagonal
    return not is_perpendicular(coordinate_pair, x_co) and not is_perpendicular(
        coordinate_pair, y_co
    )


def calc_distance(coordinate_pair):
    first, second = get_coordinate_pairs(coordinate_pair)
    a = abs(first[x_co] - second[x_co])
    b = abs(first[y_co] - second[y_co])
    c = (a + b) / 2 if is_diagonal(coordinate_pair) else a + b
    return int(c)


def resolve_index(steps, step_index):
    return 0 if len(steps) == 1 else step_index


def mark_map(result, value):
    distance = calc_distance(value)
    x_steps = [*get_index_range(value, y_co)]
    y_steps = [*get_index_range(value, x_co)]

    for step_index in range(distance + 1):
        step = (
            x_steps[resolve_index(x_steps, step_index)],
            y_steps[resolve_index(y_steps, step_index)],
        )
        map_value = result[step[x_co]][step[y_co]]
        result[step[x_co]][step[y_co]] = map_mark_handler(map_value)

    return result


def process(iterable, map_diagram):
    return reduce(mark_map, iterable, map_diagram)


def print_map_diagram(map_diagram):
    for row in map_diagram:
        print(row)


def count_map(map_diagram):
    print_map_diagram(map_diagram)
    return sum(
        map(
            lambda x: reduce(
                lambda result, x: result + 1
                if isinstance(x, int) and x > 1
                else result,
                x,
                0,
            ),
            map_diagram,
        )
    )


def main():
    print(
        count_map(
            process(
                compose(
                    get_horizontal_vertical_iter,
                    get_coordinates_iter,
                    get_data,
                )("day_5_data.txt"),
                # )("day_5_test_data.txt"),
                get_initial_map(1000, 1000),
                # get_initial_map(10, 10),
            )
        )
    )


if __name__ == "__main__":
    main()

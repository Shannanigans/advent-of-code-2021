from utils import get_data, compose, peak_compose
from day_5_part_1 import count_map, process, get_coordinates_iter, get_initial_map


def main():
    compose(
        peak_compose(lambda x: print("Answer: ", x)),
        count_map,
        process(get_initial_map(1000, 1000)),
        get_coordinates_iter,
        get_data,
    )("day_5_data.txt"),


if __name__ == "__main__":
    main()

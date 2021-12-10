from utils import get_data, compose
from day_5_part_1 import count_map, process, get_coordinates_iter, get_initial_map


def main():
    print(
        count_map(
            process(
                compose(
                    get_coordinates_iter,
                    get_data,
                )("day_5_data.txt"),
                get_initial_map(1000, 1000),
            )
        )
    )


if __name__ == "__main__":
    main()

from utils import get_data, compose, bin_to_decimal
from functools import reduce
from collections import Counter


def get_initial_state():
    return {"total_count": 0, "bin": Counter()}


def count_ones(result, value):
    for index in range(len(value)):
        digit = int(value[index])
        result["bin"][index] = (
            result["bin"][index] + 1 if digit == 1 else result["bin"][index]
        )
    result["total_count"] = result["total_count"] + 1
    return result


def answer(final_result):
    total_count = final_result["total_count"]
    gamma_rate = list(
        map(
            lambda x: 1 if x[1] > (total_count / 2) else 0,
            sorted(final_result["bin"].items()),
        )
    )
    epsilon_rate = list(map(lambda x: 0 if x == 1 else 1, gamma_rate))
    return bin_to_decimal(gamma_rate) * bin_to_decimal(epsilon_rate)


def process(file_path, initial_state):
    return reduce(count_ones, compose(get_data)(file_path), initial_state)


def main():
    # print(answer(process("day_3_test_data.txt", get_initial_state())))  # 198
    print(answer(process("day_3_data.txt", get_initial_state())))  # 2640986


if __name__ == "__main__":
    main()

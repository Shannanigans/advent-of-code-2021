from functools import reduce, partial


def get_data(filename="day-1-data.txt"):
    for line in open(filename, "r"):
        yield line.strip()


is_increase = lambda current, previous: previous is not None and current > previous


def process_part_one(result, value):
    numeric_value = int(value)
    if is_increase(numeric_value, result["previous"]):
        result["count"] = result["count"] + 1
    result["previous"] = numeric_value
    return result


get_part_one_result = lambda file_path: reduce(
    process_part_one, get_data(file_path), {"count": 0, "previous": None}
)


# print(get_part_one_result("day-1-test-data.txt"))
# print(get_part_one_result("day-1-data.txt"))


# PART 2


def process_part_two(slide_num, result, value):
    # Convert value from string
    numeric_value = int(value)

    # Append newest value
    result["previous"] = [numeric_value] + result["previous"]

    if len(result["previous"]) == slide_num + 1:

        # Determine window sums
        previous_sum = sum(result["previous"][0:slide_num])
        current_sum = sum(result["previous"][1 : slide_num + 1])

        # Increase count if increased
        if is_increase(previous_sum, current_sum):
            result["count"] = result["count"] + 1

        # Pop oldest value
        result["previous"] = result["previous"][0 : len(result["previous"]) - 1]

    return result


get_part_two_result = lambda file_path: reduce(
    partial(process_part_two, 3), get_data(file_path), {"count": 0, "previous": []}
)


# print(get_part_two_result("day-1-test-data.txt"))
print(get_part_two_result("day-1-data.txt"))

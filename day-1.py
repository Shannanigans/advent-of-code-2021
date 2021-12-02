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


def toInt(iterable):
    for x in iterable:
        yield int(x)


def take(iterable, take_num):
    take_list = []
    for x in iterable:
        # add
        take_list = [x] + take_list
        # remove
        take_list = take_list[0:take_num]
        # yield if full
        if len(take_list) == take_num:
            yield take_list


def isSumIncrease(slide_num, values):
    previous_sum = sum(values[0 : slide_num - 1])
    current_sum = sum(values[1:slide_num])
    return is_increase(previous_sum, current_sum)


def process_part_two(slide_num, file_path):
    return reduce(
        lambda result, values: result + 1
        if isSumIncrease(slide_num, values)
        else result,
        take(toInt(get_data(file_path)), slide_num),
        0,
    )


print(process_part_two(4, "day-1-test-data.txt"))
print(process_part_two(4, "day-1-data.txt"))